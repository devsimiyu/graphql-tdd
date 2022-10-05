from urllib import parse
from furl import furl
import requests

def searchPeople(page, search):
    url = 'https://swapi.dev/api/people'
    params = {
        'page': page,
        'search': search
    }
    response = requests.get(url, params)
    data = response.json()
    total = data.get('count', 0)
    next = data.get('next')
    previous = data.get('previous')
    people = map(lambda x: {
        'name': x['name'],
        'height': x['height'],
        'mass': x['mass'],
        'gender': x['gender'],
        'homeworld': x['homeworld']
    }, data.get('results', []))
    return {
        'total': total,
        'next': furl(next).args['page'] if next else None,
        'previous': furl(previous).args['page'] if previous else None,
        'result': people
    }
