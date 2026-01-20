# Security

BLUX Commander emphasizes safe-by-default observability.

## Principles

- **Least Privilege** – dashboards run without execution, enforcement, or token issuance.
- **Auditability** – telemetry trails surface audits and traces for review.
- **Isolation** – no shell execution or subprocess invocation is permitted.
- **Integrity** – plugins are metadata-only and do not mutate system state.

## Hardening Checklist

1. Restrict dashboard deployment to read-only networks or VPCs.
2. Enable TLS termination for the FastAPI server when exposed over networks.
3. Monitor observability feeds for anomalous activity.
