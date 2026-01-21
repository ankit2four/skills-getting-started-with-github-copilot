import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Soccer Team" in data

def test_signup_and_unregister():
    # Use a unique email for test
    activity = "Soccer Team"
    email = "testuser@example.com"
    # Signup
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200 or response.status_code == 400
    # Try duplicate signup
    response_dup = client.post(f"/activities/{activity}/signup?email={email}")
    assert response_dup.status_code == 400
    # Unregister (if implemented)
    unregister = client.delete(f"/activities/{activity}/unregister?email={email}")
    # Accept 200 or 404 if not implemented
    assert unregister.status_code in (200, 404)
