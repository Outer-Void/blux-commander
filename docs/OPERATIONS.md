# Operations

## Commander CLI

Use `bluxq cmd` to access read-only views:

- `dashboard` – start the Textual cockpit.
- `status` – review subsystem heartbeat information.
- `plugins list` – enumerate registered plugin modules.
- `telemetry tail` – stream recent telemetry entries.

## Runtime Modes

1. **Local Operator** – run the cockpit on a workstation for observation.
2. **Headless Observer** – run the FastAPI service for remote read-only insights.
3. **Hybrid** – use the TUI as a front-end while the API serves dashboards.

## Read-Only Guardrails

Commander does not launch terminals, execute commands, or issue tokens. It only renders observability
artifacts such as envelope, guard_receipt, execution_manifest, audits, and traces.
