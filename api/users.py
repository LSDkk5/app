from flask_restful import Resource
from flask import Blueprint, request, jsonify, abort

from web.models import User as UserModel
from web import api

api_users = Blueprint('api_users', __name__)


class UserList(Resource):
    def get(self):
        return jsonify([dict(username=u.username, email=u.email, comfirmed=u.confirmed,
        registered_date=u.registered_date) for u in UserModel.objects().all()])

class User(Resource):
    def get(self, username):
        user = UserModel.objects(username=username).first_or_404()
        return jsonify(user=dict(username=user.username, email=user.email, 
            confirmed=user.confirmed, regstered_date=user.registered_date))

api.add_resource(UserList, '/api/v1.0/users')
api.add_resource(User, '/api/v1.0/users/<username>')
