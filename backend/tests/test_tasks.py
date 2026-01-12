from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_create_task():
    res = client.post("/tasks", json={"title": "Test task"})
    assert res.status_code == 200
    assert res.json()["title"] == "Test task"


def test_list_tasks():
    res = client.get("/tasks")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
