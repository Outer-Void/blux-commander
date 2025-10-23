# API Reference

## CLI Commands

| Command | Description |
|---------|-------------|
| `bluxq cmd dashboard` | Launch the Textual cockpit. |
| `bluxq cmd shell` | Start the AI developer sandbox shell. |
| `bluxq cmd status` | Display current subsystem status information. |
| `bluxq cmd plugins list` | List registered Commander plugins. |
| `bluxq cmd telemetry tail` | Tail telemetry events in real-time. |

## HTTP Endpoints

The FastAPI service (see `blux_commander/core/api.py`) exposes the following base endpoints:

- `GET /health` – returns overall commander health.
- `GET /status` – returns subsystem status snapshot.
- `POST /commands` – executes a named command workflow.
- `GET /metrics` – surfaces Prometheus metrics when enabled.

Refer to module docstrings for additional handler descriptions.
