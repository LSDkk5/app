from flask_restful import Resource
from flask import Blueprint, request, jsonify, abort
from flask_login import login_user

from web.models import User as UserModel
from web.models import Kid
from web import api, db

api_users = Blueprint('api_users', __name__)


class UserList(Resource):
    def get(self):
        return jsonify([dict(username=u.username, email=u.email, comfirmed=u.active,
        registered_date=u.registered_date) for u in UserModel.objects().all()])

class User(Resource):
    def get(self, username):
        user = UserModel.objects(username=username).first_or_404()
        return jsonify(user=dict(username=user.username, email=user.email, 
            active=user.active, regstered_date=user.registered_date))

    def put(self):
        pass
