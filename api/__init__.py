from web import api

from api.kids import Kids, KidsController
from api.users import UserList, User
from api.auth import (Login, Register, ConfirmAccount, ResendConfirmToken)

api.add_resource(Login, '/api/v1.0/auth/login')
api.add_resource(Register, '/api/v1.0/auth/register')
api.add_resource(ResendConfirmToken, '/api/v1.0/auth/resendtoken')
api.add_resource(ConfirmAccount, '/api/v1.0/auth/confirm/<confirmToken>')

api.add_resource(UserList, '/api/v1.0/users')
api.add_resource(User, '/api/v1.0/users/<username>')

api.add_resource(Kids, '/api/v1.0/user/kids')
api.add_resource(KidsController, '/api/v1.0/user/kids/kid_oid')