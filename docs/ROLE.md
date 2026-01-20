# ROLE: Read-Only Observability Cockpit

BLUX Commander is a read-only observability cockpit. It provides UI/UX for visualizing operational
artifacts and telemetry only; it is **not a control plane** and it performs **no execution**, **no
enforcement**, and **no tokens**.

## Visualized artifacts

- `blux://contracts/envelope.schema.json`
- `blux://contracts/guard_receipt.schema.json`
- `blux://contracts/execution_manifest.schema.json` (reference only)
- Audit logs (append-only JSONL), traces, spans

## Out of scope

- Execution triggers or command dispatch
- Policy decisions or enforcement
- Capability issuance or token handling
- System mutation or state changes

## CI boundary note

Only boundary checks are required; remove any build/deploy workflows not needed for read-only
observability.
