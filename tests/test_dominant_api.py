from fastapi.testclient import TestClient

from dominant.api import app

client = TestClient(app)


def test_read_about():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"About": "Load image and create a color palette"}
