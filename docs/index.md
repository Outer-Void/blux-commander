# BLUX Commander

BLUX Commander is a read-only observability cockpit for the BLUX ecosystem. It is **not a control
plane** and performs **no execution**, **no enforcement**, and **no tokens**. The UI focuses on
visibility rather than actions or orchestration. Inputs are files/artifacts produced by other repos;
Commander does not generate them. Contracts are canonical in `blux-ecosystem`; Commander references
them by contract IDs only.

## Non-capabilities

- No execution or dispatch of workflows.
- No policy enforcement or approvals/denials.
- No token issuance, verification, or signing.

## Capabilities

- **Read-Only Commander Core** – Summarize observability status and subsystem signals.
- **Multi-Pane Cockpit** – Operate a Textual dashboard featuring logs, telemetry, and artifact explorers.
- **Web Dashboard** – Browse read-only insights through FastAPI + React.
- **Artifact Visualization** – Inspect envelope, discernment_report, guard_receipt,
  execution_manifest, audit events/logs, and traces.

See the full documentation tree for deployment, operations, and customization details.
