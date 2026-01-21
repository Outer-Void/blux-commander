# BLUX Commander

> BLUX Commander — Read-only observability cockpit

The bridge between mind and machine. The map that moves.

## Overview

BLUX Commander delivers a unified read-only observability cockpit for the BLUX ecosystem. It is
**not a control plane** and performs **no execution**, **no enforcement**, and **no tokens**.
Developers and operators can visualize envelopes, guard_receipt artifacts, execution_manifest
records, discernment_report summaries, audit events/logs, and system status without triggering
actions. Inputs are files and artifacts produced by other repos; BLUX Commander does not generate
them. Contracts are canonical in `blux-ecosystem`; Commander references them by contract IDs only.

**Non-capabilities**

- No execution or dispatch of workflows.
- No policy enforcement or approvals/denials.
- No token issuance, verification, or signing.

### Highlights

- **Read-Only Commander Core** – Aggregate observability status and artifact metadata.
- **Multi-Pane Cockpit** – Operate a Textual dashboard for logs, telemetry, and artifact views.
- **Web Dashboard** – Serve a FastAPI + React cockpit for read-only insights.
- **Artifact Explorer** – Visualize envelope, discernment_report, guard_receipt, execution_manifest,
  audit events/logs, and traces.

<!-- FILETREE:BEGIN -->
<details><summary><strong>Repository File Tree</strong></summary>

```text
├── .github
│   └── workflows
│       └── ci.yml
├── .gitignore
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── blux_commander
│   ├── __init__.py
│   ├── cli.py
│   ├── core
│   │   ├── api.py
│   │   ├── commander.py
│   │   ├── config.py
│   │   ├── plugins.py
│   │   ├── terminal.py
│   │   ├── telemetry.py
│   │   └── tui.py
│   ├── integrations
│   │   ├── ca.py
│   │   ├── doctrine.py
│   │   └── quantum.py
│   ├── ui
│   │   ├── panels
│   │   │   ├── ai_panel.py
│   │   │   ├── logs_panel.py
│   │   │   ├── plugins_panel.py
│   │   │   ├── telemetry_panel.py
│   │   │   └── terminal_panel.py
│   │   └── themes
│   │       ├── default.tcss
│   │       └── highcontrast.tcss
│   └── web
│       ├── insights.py
│       ├── server.py
│       ├── static
│       │   ├── app.js
│       │   └── assets
│       │       └── style.css
│       ├── storage.py
│       └── templates
│           └── index.html
├── docs
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── CONFIGURATION.md
│   ├── INSTALL.md
│   ├── INTEGRATIONS.md
│   ├── OPERATIONS.md
│   ├── ROLE.md
│   ├── ROADMAP.md
│   ├── SECURITY.md
│   ├── THEMES.md
│   ├── TROUBLESHOOTING.md
│   └── index.md
├── mkdocs.yml
├── pyproject.toml
├── scripts
│   ├── build_docs.sh
│   ├── gen_filetree.py
│   ├── physics_tests.sh
│   ├── run_tui_demo.py
│   └── update_readme_filetree.py
└── tests
    ├── test_cli.py
    ├── test_plugins.py
    ├── test_terminal.py
    ├── test_tui.py
    └── test_web_dashboard.py
```

</details>
<!-- FILETREE:END -->

Run `python scripts/update_readme_filetree.py` to regenerate the tree after modifying the project
structure.

## Quick Start

```bash
pip install -e .[dev]
bluxq cmd status
bluxq cmd dashboard
```

See the [documentation](docs/index.md) for installation, operations, and integration details.

### Web Dashboard

Run the read-only web dashboard locally with:

```bash
uvicorn blux_commander.web.server:app --reload
```

Open <http://127.0.0.1:8000/> to access the React + Tailwind UI.

## Scope / Non-goals

BLUX Commander is a read-only observability cockpit. It is **not a control plane** and performs
**no execution**, **no enforcement**, and **no tokens**. Inputs are file-based artifacts produced
by other repos; Commander does not generate them. It displays envelope, discernment_report,
guard_receipt, execution_manifest, and audit events/logs. Contracts are canonical in
`blux-ecosystem`; Commander references them by contract IDs only. See [docs/ROLE.md](docs/ROLE.md)
for the full scope and boundary checks.
