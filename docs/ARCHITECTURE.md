# Architecture

BLUX Commander is organized into modular layers that coordinate read-only observability,
presentation, and data feeds.

## Core Layer

- **Commander Hub (`blux_commander/core/commander.py`)** – Maintains runtime context for
  observability artifacts.
- **Shell (`blux_commander/core/shell.py`)** – Disabled placeholder that rejects execution.
- **TUI (`blux_commander/core/tui.py`)** – Exposes Textual-powered cockpit panes.
- **API (`blux_commander/core/api.py`)** – Hosts FastAPI services for read-only dashboards.
- **Telemetry (`blux_commander/core/telemetry.py`)** – Records metrics and audit trails.
- **Config (`blux_commander/core/config.py`)** – Loads configuration from env, user, and project.
- **Plugins (`blux_commander/core/plugins.py`)** – Discovers, validates, and activates plugins.

## Integration Layer

Subsystem adapters in `blux_commander/integrations/` expose read-only hooks that publish
observability artifacts into the core state.

## Presentation Layer

- **Textual UI** – Multi-pane layout containing logs, telemetry, and plugin views.
- **Web Dashboard** – Optional FastAPI + template powered read-only interface.

## Data Layer

Telemetry and audit logs are displayed for situational awareness. Data is presented as read-only
snapshots to avoid mutating system state.
