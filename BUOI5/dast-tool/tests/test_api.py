import pytest
from app import app


@pytest.mark.parametrize('endpoint', ['monitor', 'memory', 'network', 'security'])
def test_get_endpoints(endpoint):
    response = app.test_client().get('/api/' + endpoint)
    assert response.status_code == 200
    assert response.is_json


def test_sandbox_api():
    client = app.test_client()
    response = client.post('/api/sandbox', json={'command': 'echo Hello API'})
    assert response.status_code == 200
    assert response.json['stdout'].strip() == 'Hello API'
    assert client.get('/api/security').json['suspicious_calls']


@pytest.mark.parametrize('data', [{}, [], {'command': 'whoami'}, {'command': 42}])
def test_bad_request(data):
    assert app.test_client().post('/api/sandbox', json=data).status_code == 400
