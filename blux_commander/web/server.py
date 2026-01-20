"""BLUX Commander web dashboard server."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from blux_commander.core import commander, plugins

from .storage import default_storage_dir


BASE_DIR = default_storage_dir()

app = FastAPI(title="BLUX Commander Web Dashboard", version="0.2.0")
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

INDEX_FILE = Path(__file__).parent / "templates" / "index.html"


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    if not INDEX_FILE.exists():
        raise HTTPException(status_code=500, detail="Dashboard template missing")
    return HTMLResponse(INDEX_FILE.read_text(encoding="utf-8"))


@app.get("/api/status")
async def status() -> dict:
    return {
        "app": "blux-commander",
        "version": app.version,
        "cli_available": False,
        "config_dir": str(BASE_DIR),
        "subsystems": commander.state.subsystems,
    }


@app.get("/api/plugins")
async def list_plugins() -> dict:
    discovered = plugins.list_registered(verbose=False)
    return {"plugins": discovered}
