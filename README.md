# BLUX Commander

> BLUX Commander — Enterprise Developer & AI Orchestration Cockpit

The bridge between mind and machine. The map that moves.

## Overview

BLUX Commander delivers a unified cockpit for orchestrating the BLUX ecosystem. Developers and
operators can visualize subsystems, run AI-assisted terminals, and automate workflows across
Guard, Lite, Doctrine, Quantum, cA, and Reg components.

### Highlights

- **Commander Core** – Chain BLUX workflows while sharing runtime context.
- **Multi-Pane Cockpit** – Operate a Textual dashboard with terminal, logs, telemetry, and plugin panes.
- **AI Developer Shell** – Launch sandboxed Python and system environments.
- **Commander API** – Expose orchestration endpoints over FastAPI.
- **Plugin Framework** – Discover, validate, and execute external modules.
- **Telemetry Dashboard** – Capture metrics via SQLite/JSONL and Prometheus exporters.

<!-- FILETREE:BEGIN -->
<details><summary><strong>Repository File Tree</strong></summary>

```text
├── .github
│   └── workflows
│       ├── ci.yml
│       ├── docs.yml
│       └── release.yml
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
│   │   ├── shell.py
│   │   ├── telemetry.py
│   │   └── tui.py
│   ├── integrations
│   │   ├── ca.py
│   │   ├── doctrine.py
│   │   ├── guard.py
│   │   ├── lite.py
│   │   ├── quantum.py
│   │   └── reg.py
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
│       ├── server.py
│       ├── static
│       │   └── assets
│       │       └── style.css
│       └── templates
│           └── index.html
├── docs
│   ├── API.md
│   ├── ARCHITECTURE.md
│   ├── CONFIGURATION.md
│   ├── INSTALL.md
│   ├── INTEGRATIONS.md
│   ├── OPERATIONS.md
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
│   ├── run_tui_demo.py
│   └── update_readme_filetree.py
└── tests
    ├── fixtures
    ├── test_cli.py
    ├── test_plugins.py
    ├── test_shell.py
    └── test_tui.py
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

## Licensing

BLUX Commander is dual-licensed. For open-source use, it is available under the Apache License 2.0
as described in [LICENSE-APACHE](LICENSE-APACHE) and the accompanying [NOTICE](NOTICE). Commercial
or proprietary use requires a separate agreement under the terms in
[LICENSE-COMMERCIAL](LICENSE-COMMERCIAL).

### Open-source (Apache-2.0)
You may use, modify, and distribute the project under the Apache License 2.0, provided you include
the required notices and comply with the terms outlined in [LICENSE-APACHE](LICENSE-APACHE).

### Commercial licensing
If you want to embed, distribute, or monetize BLUX Commander beyond what Apache-2.0 permits, you
must obtain a commercial license. Contact theoutervoid@outlook.com to discuss terms.
