from flask import Blueprint, request, jsonify, abort, render_template, url_for
from flask_login import login_user, current_user
from flask_restful import Resource
from datetime import datetime

from utils.token import generate_confirmation_token, confirm_token
from utils.send_email import send_email
from web import bcrypt, db, api
from web.models import User


api_auth = Blueprint('api_auth', __name__)


class Login(Resource):
    def post(self):
        loginData = {
            'username': request.json['username'],
            'password': request.json['password']}
        if loginData['username'] is None or loginData['password'] is None:
            return abort(403, description='Brakujące argumenty, prosze wypełnić wszystkie pola.')
        user = User.objects(username=loginData['username']).first()
        if user and bcrypt.check_password_hash(
            user.password, loginData['password']):
            login_user(user)
        else:
            return abort(401, description='Dane logowania są niepoprawne! Spradz poprawność wprowadzonych danych!')
        return jsonify(message='Zostałeś pomyślnie zalogowany do serwisu!')

class Register(Resource):
    def post(self):
        registerData = {
            'username': request.json['username'],
            'password': request.json['password'],
            'email': request.json['email'],
            'sex': request.json['sex']}
        user = User.objects(username=registerData['username']).first()
        userEmail = User.objects(email=registerData['email']).first()

        if user:
            return abort(403, description='Użytkownik o podanej nazwie już istnieje!')
        elif userEmail:
            return abort(403, description='Konto o podanym adresie email już istnieje! prosimy o podanie innego.')
        if not registerData['username'] or registerData['password'] or registerData['email'] or registerData['sex']:
            return abort(403, description='Brakujące argumenty, prosze wypełnić wszystkie pola.')
        newUser = User(
            username=registerData['username'],
            password=bcrypt.generate_password_hash(
                registerData['password']),
            email=registerData['email'],
            sex=registerData['sex']).save()
        token = generate_confirmation_token(newUser.email)
        send_email(
            newUser.email,
            'Aktywacja Konta',
            render_template(
                'auth/activate.html',
                confirm_url=url_for(
                    'auth.confirm_account',
                    token=token,
                    _external=True)))
        return jsonify(message='Twoje konto zostało pomyślnie utworzone! Na adres e-mail została wysłana wiadomość z linkiem aktywacyjnym - prosimy aktywować konto.')

class ConfirmAccount(Resource):
    def post(self, confirmToken):
        try:
            emailp = confirm_token(confirmToken)
        except BaseException:
            return abort(403, description='Token aktywujący wygasł, lub jest niepoprawny!')
        # if not emailp: return abort(403, description='Coś poszło nie tak, skontaktuj sie z administratorem serwisu!')
        user = User.objects(username='LSD').first_or_404()
        if user.confirmed:
            return abort(403, description='To konto zostało już aktywowane.')
        else: 
            user.update(confirmed=True)
        return jsonify(message='Konto zostało pomyślnie aktywowane! Dziękujemy')

class ResendConfirmToken(Resource):
    def get(self):
        user = User.objects(username='LSD').first()
        login_user(user)
        if not current_user.is_authenticated:
            return abort(403)
        if current_user.confirmed:
            return abort(403)
        user = User.objects(username=current_user.username).first_or_404()
        token = generate_confirmation_token(user.email)
        send_email(
            user.email,
            'Aktywacja Konta',
            render_template(
                'auth/activate.html',
                confirm_url=url_for(
                    'auth.confirm_account',
                    token=token,
                    _external=True)))
        return jsonify(message='Na twoj adres email został wysłany link potwierdzający!')
