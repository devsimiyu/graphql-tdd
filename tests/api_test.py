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


def test_listPosts(http_client):
    response = http_client.post(
        '/graphql',
        data=json.dumps({
            'query': '''
                query getPosts {
                    listPosts {
                        id
                        title
                    }
                }
            '''
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    assert json.loads(response.data) == {"data":{"listPosts":[{"id":"1","title":"post 1"},{"id":"2","title":"post 2"}]}}


def test_getPost(http_client):
    response = http_client.post(
        '/graphql',
        data=json.dumps({
            'query': '''
                query findPost($id: ID!) {
                    getPost(id: $id) {
                        id,
                        title,
                        description
                    }
                }
            ''',
            'variables': {
                'id': 0
            }
        }),
        content_type='application/json'
    )
    assert response.status_code == 200
    assert json.loads(response.data) == {'data': {'getPost': {'description': 'post desc 1', 'id': '1', 'title': 'post 1'}}}
