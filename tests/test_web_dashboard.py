from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator

import pytest
from fastapi.testclient import TestClient


MODULES_TO_CLEAR = [
    "blux_commander.web.server",
    "blux_commander.web.storage",
    "blux_commander.web.insights",
]


@pytest.fixture()
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[TestClient]:
    config_dir = tmp_path / ".config" / "blux-commander"
    monkeypatch.setenv("BLUX_COMMANDER_HOME", str(config_dir))
    import importlib

    for module in MODULES_TO_CLEAR:
        sys.modules.pop(module, None)
    server = importlib.import_module("blux_commander.web.server")
    with TestClient(server.app) as test_client:
        yield test_client


def test_status_endpoint(client: TestClient) -> None:
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert data["app"] == "blux-commander"
    assert "subsystems" in data


def test_plugins_endpoint(client: TestClient) -> None:
    response = client.get("/api/plugins")
    assert response.status_code == 200
    assert "plugins" in response.json()
