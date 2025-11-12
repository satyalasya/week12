import pytest
from app import app

@pytest.fixture
def client():
    # Create a test client using Flask’s built-in testing feature
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Find your next stay" in response.data  # optional content check
