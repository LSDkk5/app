from flask_login import LoginManager, AnonymousUserMixin
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_restful import Api
from flask_mail import Mail
from flask_cors import CORS
from flask import Flask


from settings import Settings

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Settings)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
login_manager = LoginManager(app)
db = MongoEngine(app)
bcrypt = Bcrypt(app)
mail = Mail(app)
api = Api(app)



from web.profile.routes import profile
from web.home.routes import home
from web.auth.routes import auth

from api.auth import api_auth
from api.users import api_users

app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(profile)
app.register_blueprint(api_auth)
app.register_blueprint(api_users)
