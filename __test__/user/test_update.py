from fastapi.testclient import TestClient
from dotenv import load_dotenv
import pytest
from __test__.user.factory.user import user, update_user
from src.models.base import Base
from src.db import engine
from src.app import app

load_dotenv('.env.test')



@pytest.fixture(autouse=True)
def run_around_tests():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

client = TestClient(app)

def init():
    data = user()
    response = client.post("/api/v1/user", json=data)
    return response.json()

def test_update_valid_user():
    registered = init()
    data = update_user()
    response = client.put("/api/v1/user/"+registered['id'], json=data)
    response_data = response.json()
    print(response_data)
    assert response.status_code == 200
    assert response_data['message'] == 'Success'
    assert response_data['status'] == 200

def test_update_not_found_user():
    data = update_user()
    response = client.put("/api/v1/user/807f09d0-cc9f-4490-9a1c-7c32eabf21a2", json=data)
    assert response.status_code == 404
    response_data = response.json()
    assert response_data['message'] == 'Not found'
    assert response_data['status'] == 404

def test_update_with_invalid_attributes_user():
    registered = init()
    data = user()
    response = client.put("/api/v1/user/"+registered['id'], json=data)
    assert response.status_code == 404
    response_data = response.json()
    assert response_data['message'] == 'Not found'
    assert response_data['status'] == 404