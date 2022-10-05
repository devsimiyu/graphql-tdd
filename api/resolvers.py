import os
from api.auth import auth
from repository import starwars_repo
import jwt


def authenticate_resolver(obj, info, username):
    secret = os.environ['JWT_SECRET']
    token = jwt.encode({
        'username': username
    }, secret, algorithm='HS256')
    return {
        'token': token
    }


@auth
def getPeople_resolver(obj, info, page, search=None):
    return starwars_repo.searchPeople(page, search)
