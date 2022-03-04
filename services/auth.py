from functools import wraps
import firebase_admin
from firebase_admin import credentials, auth
from flask import request



def build_firebase_app():
    cred = credentials.Certificate("./service_account.json")
    firebase_admin.initialize_app(cred)

build_firebase_app()

def check_token(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        token = request.headers.get('authorization')

        if not token:
            return {'message': 'No authorization token provided'}, 401
        try:
            user = auth.verify_id_token(token)
            request.user = user
        except:
            return {'message':'Invalid authorization token provided'}, 401
        return f(*args, **kwargs)
    return wrap