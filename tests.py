import pytest
from flask import *
from capitalise import *
from app import app

# Unit Tests
def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)

# Integration tests
@pytest.fixture
def client():
    return app.test_client()

def test_home_returns_200(client):
    resp = client.get('/home')
    assert resp.status_code == 200

def test_home(client):
    resp = client.get('/home')
    assert resp.data == b"<h1>Welcome to your capitalising app!</h1>"

def test_capitalise_dog(client):
    resp = client.get('/capitalise/dog')
    assert b"<h2>Capitalise Dog</h2>" in resp.data
