# BLUX Commander Role

## Mission

BLUX Commander is a **read-only observability cockpit** for the BLUX ecosystem. It **is not a
control plane** and it performs **no execution**.

## Allowed artifacts (display-only)

BLUX Commander may only display and visualize the following artifacts:

- traces
- envelopes
- guard_receipts
- execution_manifests
- audits
- status

## Explicit non-goals

BLUX Commander must never:

- execute commands, tools, or workflows
- issue, verify, or manage tokens of any kind
- enforce policy or implement a policy engine
- act as a runner, scheduler, or execution engine
- mutate system state or reach into host controls

## Boundary checks

Repository CI includes physics tests that block execution primitives, state mutation intent, and
role-bleed keywords in code directories.
