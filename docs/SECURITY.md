# Security

BLUX Commander emphasizes safe-by-default orchestration.

## Principles

- **Least Privilege** – subsystems run with constrained permissions and scoped API tokens.
- **Auditability** – telemetry trails capture who executed which workflows and when.
- **Sandboxing** – the developer shell isolates processes with environment filters.
- **Integrity** – plugins must declare capabilities and are validated before activation.

## Hardening Checklist

1. Configure OS-level sandboxing (Firejail, AppArmor, or Windows Defender Application Control).
2. Store secrets in platform keyrings and inject via environment variables.
3. Enable TLS termination for the FastAPI server when exposed over networks.
4. Monitor the Prometheus metrics endpoint for anomalous activity.
