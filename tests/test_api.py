from typing import Generator

import pytest
from fastapi.testclient import TestClient

from genai_scaffolding_pro.api.main import create_app


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    """Typed TestClient fixture (yields, then closes cleanly)."""
    with TestClient(create_app()) as c:
        yield c


def test_health(client: TestClient) -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_invoke_agent_valid(client: TestClient) -> None:
    payload = {"input": "Hello world", "params": {"model": "gpt-5"}}
    resp = client.post("/v1/agents/researcher/invoke", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["agent"] == "researcher"
    assert data["output"]["echo"] == "Hello world"
    assert data["meta"]["model"] == "gpt-5"


def test_invoke_agent_empty_input(client: TestClient) -> None:
    payload = {"input": "   "}
    resp = client.post("/v1/agents/researcher/invoke", json=payload)
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Empty input"
