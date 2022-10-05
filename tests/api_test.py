import json
from app import app
import pytest


@pytest.fixture(scope='module')
def http_client():
    return app.test_client()


def test_health(http_client):
    response = http_client.get('/health')
    assert response.status_code == 200
    assert response.data == b'Hello, world!'


def test_getPeople(http_client):
    response = http_client.post(
        '/graphql',
        data=json.dumps({
            'query': '''
                query fetchPeople($page: Int!, $search: String) {
                    getPeople(page: $page, search: $search) {
                        count
                        next
                        previous
                        results {
                            name
                            gender
                            homeworld
                            height
                            mass
                        }
                    }
                }
            ''',
            'variables': {
                'page': 1,
                'search': 'Luke'
            }
        }),
        content_type='application/json'
    )
    assert response.status_code == 200


def test_authenticate(http_client):
    response = http_client.post(
        '/graphql',
        data=json.dumps({
            'query': '''
                mutation login($username: String!) {
                    authenticate(username: $username) {
                        token
                    }
                }
            ''',
            'variables': {
                'username': 'imrsqd',
            }
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
