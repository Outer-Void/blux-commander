# Architecture

BLUX Commander is organized into modular layers that coordinate orchestration, presentation,
and integrations.

## Core Layer

- **Commander Hub (`blux_commander/core/commander.py`)** – Maintains runtime context, event bus,
  and workflow chaining.
- **Shell (`blux_commander/core/shell.py`)** – Provides the AI developer sandbox abstraction.
- **TUI (`blux_commander/core/tui.py`)** – Exposes Textual-powered cockpit panes.
- **API (`blux_commander/core/api.py`)** – Hosts FastAPI services for remote control.
- **Telemetry (`blux_commander/core/telemetry.py`)** – Records metrics and audit trails.
- **Config (`blux_commander/core/config.py`)** – Loads configuration from env, user, and project.
- **Plugins (`blux_commander/core/plugins.py`)** – Discovers, validates, and activates plugins.

## Integration Layer

Subsystem adapters in `blux_commander/integrations/` expose `register(commander)` hooks that bind
Guard, Lite, Doctrine, Quantum, cA, and Reg capabilities into the core event system.

## Presentation Layer

- **Textual UI** – Multi-pane layout containing terminal, logs, telemetry, AI, and plugin views.
- **Web Dashboard** – Optional FastAPI + template powered remote interface.

## Data Layer

Telemetry and audit logs are persisted to JSONL or SQLite via `sqlite-utils`, while Prometheus
metrics provide operational insight. Configuration merges at runtime to deliver deterministic
bootstrapping.
