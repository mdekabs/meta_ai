import pytest
from app import create_app

def test_index_route():
    app = create_app()
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Medical Assistant AI is up and running!" in response.data

def test_chat_endpoint_valid_message():
    app = create_app()
    client = app.test_client()
    valid_message = {"message": "I have a headache."}
    response = client.post('/chat', json=valid_message)
    assert response.status_code == 200
    assert b"response" in response.data

def test_chat_endpoint_invalid_input():
    app = create_app()
    client = app.test_client()
    invalid_message = {"msg": "Hello"}  # Missing "message" key
    response = client.post('/chat', json=invalid_message)
    assert response.status_code == 400
    assert b"Invalid input or missing required fields" in response.data
