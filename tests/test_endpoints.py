from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_classify_journal_entry():
    response = client.post("/api/v1/classify", json={"text": "I felt grateful today for my family's support."})
    assert response.status_code == 200
    assert "scores" in response.json()
