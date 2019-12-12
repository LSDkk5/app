from flask import Blueprint, render_template
from flask_login import current_user

from web.models import User

profile = Blueprint('profile', __name__)

@profile.route('/profile', methods=['POST', 'GET'])
def current_user_profile():
    if current_user.is_authenticated:
        user = User.objects(username=current_user.username).first()
    else: return 404
    return render_template('profile/profile.html', user=user)

@profile.route('/profile/<username>', methods=['POST', 'GET'])
def user_profile(username):
    return render_template('profile/profile.html', 
            user=User.objects(username=username).first_or_404())