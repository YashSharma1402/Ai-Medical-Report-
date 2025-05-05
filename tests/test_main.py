from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze():
    response = client.post("/analyze", json={"content": "This patient has diabetes."})
    assert response.status_code == 200
    assert "diabetes" in response.json()["summary"].lower()
