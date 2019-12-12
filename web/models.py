from flask_login import UserMixin
from datetime import datetime
from bson.objectid import ObjectId

from web import app, db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Kid(db.EmbeddedDocument):
    oid = db.ObjectIdField(required=True, default=ObjectId,
                    unique=True, primary_key=True)
    name = db.StringField()
    height = db.IntField()
    sex = db.StringField(max_length=1)
    age = db.IntField()
    shoe_size = db.IntField()
    favorite_colour = db.StringField()

class FollowedOffers(db.EmbeddedDocument):
    oid = db.ObjectIdField(required=True, default=ObjectId,
                    unique=True, primary_key=True)


class User(UserMixin, db.Document):
    username = db.StringField(unique=True)
    password = db.StringField()
    email = db.EmailField(unique=True)
    preferences = db.ListField()
    kids = db.ListField(db.EmbeddedDocumentField(Kid))
    intrests = db.ListField()
    sex = db.StringField(max_length=1)
    registered_date = db.DateTimeField(default=datetime.now())
    followed_offers = db.ListField(db.EmbeddedDocumentField(FollowedOffers))
    confirmed = db.BooleanField(default=False)
    last_password_change = db.DateTimeField(null=True)
    avatar_path = db.StringField(default='/static/images/users/default.png')

class Offers(db.Document):
    pass