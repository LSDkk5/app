from flask_login import UserMixin
from datetime import datetime

from web import app, db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# class User(db.Model, UserMixin):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(25), unique=True, nullable=False)
#     email = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     registered_on = db.Column(db.String(10), nullable=False)
#     registered_time = db.Column(db.String(5), nullable=True)
#     confirmed = db.Column(db.Boolean, nullable=False, default=False)
#     last_change = db.Column(db.DateTime, nullable=True)
#     avatar_path = db.Column(
#         db.String(100),
#         unique=False,
#         nullable=False,
#         default='/static/images/users/default.png')

#     def __repr__(self):
#         return f"{self.id}, {self.username}, {self.email}"

class User(UserMixin, db.Document):
    username = db.StringField(unique=True)
    email = db.EmailField(unique=True)
    password = db.StringField()
    registered_date = db.DateTimeField(default=datetime.now())
    followed_offers = db.ListField()
    confirmed = db.BooleanField(default=False)
    last_password_change = db.DateTimeField(null=True)
    avatar_path = db.StringField(default='/static/images/users/default.png')