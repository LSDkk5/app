from flask import request, jsonify
from flask_restful import Resource

from web.models import User as UserModel
from web.models import Kid
from web import api

class AddKid(Resource):
    def post(self):
        user = UserModel.objects(username='LSD').first()
        kidData = [request.json['name'], request.json['age'], request.json['height'],
                    request.json['favorite_colour'], request.json['shoe_size']]
        for k in kidData:
            if not k: return jsonify(message='Brakujące parametry')
        if not kidData[1].isdigit() or not kidData[2].isdigit() or not kidData[4].isdigit():
            return jsonify(message='Podane wartości muszą być typu liczbowego!')
        user.kids.append(Kid(name=kidData[0], age=kidData[1], height=kidData[2], 
            favorite_colour=kidData[3],shoe_size=kidData[4]))
        user.save()
        return jsonify(message='Dziecko zostało dodane pomyślnie')
        
class GetKids(Resource):
    def get(self):
        return jsonify(kids=[dict(name=k.name, age=k.age, heigth=k.height, 
                favorite_colour=k.favorite_colour, shoe_size=k.shoe_size)
                 for k in UserModel.objects(username='LSD').first().kids])

class UpdateKid(Resource):
    def put(self, kid_oid):
        pass

class DeleteKid(Resource):
    def delete(self):
        pass

api.add_resource(AddKid, '/api/v1.0/user/kids')
api.add_resource(GetKids, '/api/v1.0/user/kids')