from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator

import pytest
from fastapi.testclient import TestClient


MODULES_TO_CLEAR = [
    "blux_commander.web.server",
    "blux_commander.web.auth",
    "blux_commander.web.commands",
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


def test_bootstrap_creates_keypair(client: TestClient) -> None:
    response = client.get("/api/auth/keypair")
    assert response.status_code == 200
    data = response.json()
    assert "public_key" in data


def test_protected_endpoints_allow_readonly_access(client: TestClient) -> None:
    response = client.get("/api/repos")
    assert response.status_code == 200


def test_command_execution_records_memory(client: TestClient) -> None:
    execute_response = client.post(
        "/api/commands/execute",
        json={"command": "plugins list"},
    )
    assert execute_response.status_code == 200
    result = execute_response.json()["result"]
    assert "exit_code" in result
    assert result["command"] == "plugins list"
    assert result["exit_code"] == 501

    memory_response = client.get("/api/memory/replay")
    assert memory_response.status_code == 200
    entries = memory_response.json()["entries"]
    assert entries, "memory should include executed command"
    assert entries[0]["command"] == "plugins list"


def test_repo_insights_roundtrip(client: TestClient, tmp_path: Path) -> None:
    repo_dir = tmp_path / "example"
    repo_dir.mkdir()
    (repo_dir / "README.md").write_text("test", encoding="utf-8")

    add_response = client.post(
        "/api/repos",
        json={"name": "Example", "path": str(repo_dir)},
    )
    assert add_response.status_code == 200

    repos_response = client.get("/api/repos")
    assert repos_response.status_code == 200
    repos = repos_response.json()["repos"]
    assert any(repo["name"] == "Example" for repo in repos)


def test_plugins_endpoint(client: TestClient) -> None:
    response = client.get("/api/plugins")
    assert response.status_code == 200
    assert "plugins" in response.json()
