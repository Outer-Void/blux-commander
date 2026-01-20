"""BLUX Commander web dashboard server."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from fastapi import Depends, FastAPI, Header, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from blux_commander.core import commander, plugins

from .auth import AuthManager, KeyPair
from .commands import CommandExecutor
from .insights import RepoIndex, RepoRecord
from .storage import StorageManager, default_storage_dir


BASE_DIR = default_storage_dir()
storage_manager = StorageManager(BASE_DIR)
auth_manager = AuthManager()
repo_index = RepoIndex(storage_manager)
command_executor = CommandExecutor(storage_manager)

app = FastAPI(title="BLUX Commander Web Dashboard", version="0.2.0")
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

INDEX_FILE = Path(__file__).parent / "templates" / "index.html"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_token_header(x_blux_key: Optional[str] = Header(default=None)) -> Optional[str]:
    return x_blux_key


def require_auth(token: Optional[str] = Depends(get_token_header)) -> KeyPair:
    return auth_manager.require(token)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    if not INDEX_FILE.exists():
        raise HTTPException(status_code=500, detail="Dashboard template missing")
    return HTMLResponse(INDEX_FILE.read_text(encoding="utf-8"))


@app.get("/api/status")
async def status() -> dict:
    keypair = auth_manager.ensure_keypair()
    return {
        "app": "blux-commander",
        "version": app.version,
        "cli_available": False,
        "config_dir": str(BASE_DIR),
        "public_key": keypair.public_key,
        "subsystems": commander.state.subsystems,
    }


@app.get("/api/auth/keypair")
async def auth_keypair() -> dict:
    keypair = auth_manager.ensure_keypair()
    return {"public_key": keypair.public_key, "mode": "read-only"}


@app.post("/api/auth/session")
async def auth_session(payload: dict) -> dict:
    _ = payload.get("token")
    return {"status": "ok", "mode": "read-only"}


@app.get("/api/commands/memory")
async def command_memory(_: KeyPair = Depends(require_auth)) -> dict:
    return {"entries": storage_manager.list_memory(limit=100)}


@app.post("/api/commands/execute")
async def command_execute(payload: dict, _: KeyPair = Depends(require_auth)) -> dict:
    command = payload.get("command")
    repo = payload.get("repo")
    if not command:
        raise HTTPException(status_code=400, detail="Command is required")
    result = command_executor.execute(command, repo)
    return {"result": result.as_dict()}


@app.websocket("/ws/commands")
async def commands_socket(websocket: WebSocket) -> None:
    _ = websocket.query_params.get("token")
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_json()
            command = message.get("command")
            repo = message.get("repo")
            if not command:
                await websocket.send_json({"type": "error", "message": "Command is required"})
                continue
            async for chunk in command_executor.stream(command, repo):
                await websocket.send_json(chunk)
    except WebSocketDisconnect:
        return


@app.get("/api/repos")
async def list_repos(_: KeyPair = Depends(require_auth)) -> dict:
    insights = [insight.as_dict() for insight in repo_index.collect_insights()]
    return {"repos": insights}


@app.post("/api/repos")
async def add_repo(payload: dict, _: KeyPair = Depends(require_auth)) -> dict:
    name = payload.get("name")
    path = payload.get("path")
    description = payload.get("description")
    if not name or not path:
        raise HTTPException(status_code=400, detail="name and path are required")
    repo_index.upsert_record(RepoRecord(name=name, path=path, description=description))
    return {"status": "ok"}


@app.delete("/api/repos/{name}")
async def delete_repo(name: str, _: KeyPair = Depends(require_auth)) -> dict:
    repo_index.remove_record(name)
    return {"status": "ok"}


@app.get("/api/plugins")
async def list_plugins(_: KeyPair = Depends(require_auth)) -> dict:
    discovered = plugins.list_registered(verbose=False)
    return {"plugins": discovered}


@app.get("/api/memory/replay")
async def memory_replay(_: KeyPair = Depends(require_auth)) -> dict:
    return {"entries": storage_manager.list_memory(limit=200)}
