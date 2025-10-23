# Configuration

Commander resolves configuration from multiple sources:

1. Environment variables (`BLUX_CMD_*`).
2. User configuration (`~/.config/blux-commander/config.yaml`).
3. Project configuration (`./config.yaml`).

Later entries override earlier ones while maintaining backward compatibility.

## Example Configuration

```yaml
default_workspace: ~/blux
telemetry:
  enabled: true
  store: sqlite
plugins:
  paths:
    - ./plugins
```

## Environment Flags

- `BLUX_CMD_TELEMETRY=off` – disable telemetry persistence.
- `BLUX_CMD_VERBOSE=true` – enable verbose logging in the CLI and TUI.
