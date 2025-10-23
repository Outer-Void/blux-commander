# Operations

## Commander CLI

Use `bluxq cmd` to access orchestration commands:

- `dashboard` – start the Textual cockpit.
- `shell` – enter the AI developer sandbox.
- `status` – review subsystem heartbeat information.
- `plugins list` – enumerate registered plugin modules.
- `telemetry tail` – stream recent telemetry entries.

## Runtime Modes

1. **Local Operator** – run everything on a workstation, ideal for development.
2. **Headless Orchestrator** – run the FastAPI service for remote control and telemetry exports.
3. **Hybrid** – use the TUI as a front-end while the API bridges to remote infrastructure.

## Safe Sandbox

The shell module launches subprocesses with configurable working directories and environment
filters. Telemetry automatically records command execution metadata.
