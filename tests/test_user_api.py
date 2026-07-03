from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "Alice", "email": "alice@example.com", "password": "password123"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Alice"
def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
def test_delete_user_not_found():
    response = client.delete("/users/999")
    assert response.status_code == 404