from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_user_onboarding_workflow():
    # Assume admin token is not required for test simplicity
    response = client.post(
        "/workflows/onboarding",
        json={"input_data": {"name": "Bob", "email": "bob@example.com", "password": "password123"}}
    )
    assert response.status_code == 200
    assert "id" in response.json()["result"]
def test_user_deletion_workflow_not_found():
    response = client.post(
        "/workflows/deletion",
        json={"input_data": {"id": 999}}
    )
    assert response.status_code == 200
    assert response.json()["result"]["error"] == "User not found"