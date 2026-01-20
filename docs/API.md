# API Reference

## CLI Commands

| Command | Description |
|---------|-------------|
| `bluxq cmd dashboard` | Launch the Textual cockpit. |
| `bluxq cmd status` | Display current subsystem status information. |
| `bluxq cmd plugins list` | List registered Commander plugins. |
| `bluxq cmd telemetry tail` | Tail telemetry events in real-time. |

## HTTP Endpoints

The FastAPI service exposes the following read-only endpoints:

- `GET /api/status` – returns subsystem status snapshot.
- `GET /api/plugins` – lists registered plugin metadata.

Refer to module docstrings for additional handler descriptions.
