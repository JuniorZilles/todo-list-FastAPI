from fastapi.testclient import TestClient
from dotenv import load_dotenv
import pytest
from __test__.user.factory.user import invalid_user, user
from src.models.base import Base
from src.db import engine
from src.app import app

load_dotenv('.env.test')



@pytest.fixture(autouse=True)
def run_around_tests():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_create_valid_user():
    data = user()
    response = client.post("/api/v1/user", json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['id'] != None
    assert response_data['email'] == data['email']
    assert response_data['name'] == data['name']
    assert response_data['cpf'] == data['cpf']
    assert response_data['birth_date'] == data['birth_date']
    assert 'password' not in response_data
    assert response_data['address'] == data['address']
    assert response_data['city'] == data['city']
    assert response_data['state'] == data['state']
    assert response_data['country'] == data['country']
    assert response_data['zip_code'] == data['zip_code']

def test_create_invalid_user():
    data = invalid_user()
    response = client.post("/api/v1/user", json=data)
    assert response.status_code == 200
    response_data = response.json()
    print(response_data)
    assert response_data['status'] == 400
    assert len(response_data['errors']) == 8

def test_create_same_cpf_user():
    data = user()
    responseInitial = client.post("/api/v1/user", json=data)
    assert responseInitial.status_code == 201
    data['email'] = 'new@mail.com'
    response = client.post("/api/v1/user", json=data)
    assert response.status_code == 409
    response_data = response.json()
    assert response_data['status'] == 409
    assert response_data['message'] == 'Resource already created'

def test_create_same_email_user():
    data = user()
    responseInitial = client.post("/api/v1/user", json=data)
    assert responseInitial.status_code == 201
    data['cpf'] = '609.612.880-78'
    response = client.post("/api/v1/user", json=data)
    assert response.status_code == 409
    response_data = response.json()
    assert response_data['status'] == 409
    assert response_data['message'] == 'Resource already created'