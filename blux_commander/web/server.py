"""Optional web dashboard server."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader, select_autoescape

from blux_commander.core import commander

app = FastAPI(title="BLUX Commander Web")
_templates_path = Path(__file__).parent / "templates"
_env = Environment(loader=FileSystemLoader(_templates_path), autoescape=select_autoescape())


@app.get("/")
async def index(request: Request) -> HTMLResponse:
    """Render the dashboard landing page."""

    template = _env.get_template("index.html")
    html = template.render(subsystems=commander.state.subsystems, request=request)
    return HTMLResponse(html)


app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
