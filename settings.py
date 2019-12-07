import secrets
import json

# db = ''
# with open('database.json', 'r') as database:
#     data = json.load(database)
#     db = (
#         data['host'],
#         data['port'],
#         data['user'],
#         data['password'],
#         data['database'])


class Settings:
    SECRET_KEY = secrets.token_hex(32)
    SECURITY_PASSWORD_SALT = secrets.token_hex(4)
    JWT_SECRET_KEY = SECRET_KEY

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = 'LSD'

    MONGODB_SETTINGS = {
        'db': 'user',
        'host': 'mongodb+srv://admin:chujkurwa@cluster0-0ehjt.mongodb.net/apitest?retryWrites=true&w=majority'
    }
