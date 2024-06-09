import pytest
from user_management import create_app
from user_management.base_model import db
from user_management.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_user(client):
    response = client.post('/users/', json={
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    })
    assert response.status_code == 201
    assert response.json['email'] == 'test@example.com'

def test_get_users(client):
    client.post('/users/', json={
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    })
    response = client.get('/users/')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_user(client):
    client.post('/users/', json={
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    })
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json['email'] == 'test@example.com'

def test_update_user(client):
    client.post('/users/', json={
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    })
    response = client.put('/users/1', json={
        'email': 'updated@example.com',
        'first_name': 'Jane',
        'last_name': 'Doe'
    })
    assert response.status_code == 200
    assert response.json['email'] == 'updated@example.com'

def test_delete_user(client):
    client.post('/users/', json={
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe'
    })
    response = client.delete('/users/1')
    assert response.status_code == 204
    response = client.get('/users/1')
    assert response.status_code == 404
