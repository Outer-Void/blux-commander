# Integrations

Commander integrations are read-only data feeds that publish observability artifacts. They do not
execute commands, enforce policy, or mutate system state.

| Feed | Description |
|------|-------------|
| Envelope stream | Surface envelope payloads for operators to inspect. |
| Execution manifest feed | Display execution_manifest records and status changes. |
| Guard receipt feed | Visualize guard_receipt artifacts emitted by upstream systems. |
| Audit trail export | Render audits and compliance traces in the cockpit. |
| Trace pipeline | Show traces and timing data for observability. |

## Integration Lifecycle

1. Commander subscribes to read-only feeds on boot.
2. Feeds emit artifacts that are visualized in the cockpit.
3. No actions are triggered from within Commander.
