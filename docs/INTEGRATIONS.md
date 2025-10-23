# Integrations

Each BLUX subsystem exposes a `register(commander)` function that can attach commands, dashboards,
and event handlers to the Commander core.

| Subsystem | Module | Capabilities |
|-----------|--------|--------------|
| Lite | `blux_commander.integrations.lite` | Launch workflows, manage task queues |
| Guard | `blux_commander.integrations.guard` | Security analysis, threat surface review |
| Quantum | `blux_commander.integrations.quantum` | Host CLI adapters and quantum job routing |
| Doctrine | `blux_commander.integrations.doctrine` | Policy enforcement and compliance checks |
| cA | `blux_commander.integrations.ca` | Reflective reasoning prompts and insights |
| Reg | `blux_commander.integrations.reg` | Capability registry access and trust mediation |

## Integration Lifecycle

1. Commander loads static integrations during boot.
2. Plugins can extend or override integration behavior at runtime.
3. Events flow through the central bus, enabling cross-subsystem coordination.
