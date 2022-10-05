from functools import wraps
import sys
from flask import request
import os
import jwt


def auth(f):

    @wraps(f)
    def decorator(*args, **kwargs):
        if 'Authorization' not in request.headers:
            raise Exception('Authorization header is required')
        try:    
            token = request.headers['Authorization'].split(' ')[1]
            secret = os.environ['JWT_SECRET']
            jwt.decode(token, secret, algorithms=['HS256'])
        except Exception as error:
            print(error, file=sys.stderr)
            raise Exception('Invalid authorization token')
        return f(*args, **kwargs)
    
    return decorator
