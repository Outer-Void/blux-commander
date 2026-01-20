"""FastAPI service exposing commander observability."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from prometheus_client import CONTENT_TYPE_LATEST, CollectorRegistry, Gauge, generate_latest
import uvicorn

from blux_commander.core import commander

app = FastAPI(title="BLUX Commander API")
_registry = CollectorRegistry()
_commander_status = Gauge("blux_commander_subsystems", "Subsystem states", ["name"], registry=_registry)


@app.on_event("startup")
async def startup() -> None:
    """Initialize commander state on startup."""

    commander.bootstrap()
    for name, status in commander.state.subsystems.items():
        _commander_status.labels(name=name).set(1 if status == "connected" else 0)


@app.get("/health")
async def health() -> dict[str, str]:
    """Return service health."""

    return {"status": "ok"}


@app.get("/status")
async def status() -> dict[str, dict[str, str]]:
    """Return subsystem status."""

    return {"subsystems": commander.state.subsystems}


@app.get("/metrics")
async def metrics() -> JSONResponse:
    """Expose Prometheus metrics."""

    payload = generate_latest(_registry)
    return JSONResponse(content=payload.decode("utf-8"), media_type=CONTENT_TYPE_LATEST)


def run(host: str = "127.0.0.1", port: int = 8000, reload: bool = False) -> None:
    """Run the API using uvicorn."""

    uvicorn.run("blux_commander.core.api:app", host=host, port=port, reload=reload)  # noqa: S104
