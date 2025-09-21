import pytest
from fastapi.testclient import TestClient
from genai_scaffolding_pro.api.main import create_app


@pytest.fixture(scope="module")
def client():
    app = create_app()
    return TestClient(app)


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_invoke_agent_valid(client):
    payload = {"input": "Hello world", "params": {"model": "gpt-5"}}
    resp = client.post("/v1/agents/researcher/invoke", json=payload)

    assert resp.status_code == 200
    data = resp.json()

    # Basic structure checks
    assert "run_id" in data
    assert data["agent"] == "researcher"
    assert "output" in data
    assert "meta" in data

    # Echo behavior check
    assert data["output"]["echo"] == "Hello world"
    assert data["meta"]["model"] == "gpt-5"


def test_invoke_agent_empty_input(client):
    payload = {"input": "   "}
    resp = client.post("/v1/agents/researcher/invoke", json=payload)

    assert resp.status_code == 400
    data = resp.json()
    assert data["detail"] == "Empty input"
