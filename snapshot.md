# Repository Snapshot

## 1) Metadata
- Repository name: blux-commander
- Organization / owner: unknown
- Default branch (if detectable): work
- HEAD commit hash (if available): 12d830c8c1d7ace962db4a79ad6cc7a16e7d2684
- Snapshot timestamp (UTC): 2026-01-22T05:17:20Z
- Total file count (excluding directories): 60
- Description: > BLUX Commander — Read-only observability cockpit

## 2) Repository Tree
.github/
  workflows/
    ci.yml [text]
.gitignore [text]
CHANGELOG.md [text]
CODE_OF_CONDUCT.md [text]
COMMERCIAL.md [text]
CONTRIBUTING.md [text]
LICENSE [text]
LICENSE-APACHE [text]
LICENSE-COMMERCIAL [text]
NOTICE [text]
README.md [text]
blux_commander/
  __init__.py [text]
  cli.py [text]
  core/
    api.py [text]
    commander.py [text]
    config.py [text]
    plugins.py [text]
    telemetry.py [text]
    terminal.py [text]
    tui.py [text]
  integrations/
    ca.py [text]
    doctrine.py [text]
    quantum.py [text]
  ui/
    panels/
      ai_panel.py [text]
      logs_panel.py [text]
      plugins_panel.py [text]
      telemetry_panel.py [text]
      terminal_panel.py [text]
    themes/
      default.tcss [text]
      highcontrast.tcss [text]
  web/
    insights.py [text]
    server.py [text]
    static/
      app.js [text]
      assets/
        style.css [text]
    storage.py [text]
    templates/
      index.html [text]
docs/
  API.md [text]
  ARCHITECTURE.md [text]
  CONFIGURATION.md [text]
  INSTALL.md [text]
  INTEGRATIONS.md [text]
  OPERATIONS.md [text]
  ROADMAP.md [text]
  ROLE.md [text]
  SECURITY.md [text]
  THEMES.md [text]
  TROUBLESHOOTING.md [text]
  index.md [text]
mkdocs.yml [text]
pyproject.toml [text]
scripts/
  build_docs.sh [text]
  gen_filetree.py [text]
  physics_tests.sh [text]
  run_tui_demo.py [text]
  update_readme_filetree.py [text]
tests/
  test_cli.py [text]
  test_plugins.py [text]
  test_terminal.py [text]
  test_tui.py [text]
  test_web_dashboard.py [text]

## 3) FULL FILE CONTENTS (MANDATORY)

FILE: .github/workflows/ci.yml
Kind: text
Size: 424
Last modified: 2026-01-22T05:15:43Z

CONTENT:
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  lint-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: python -m pip install --upgrade pip
      - run: pip install -e .[dev]
      - run: bash scripts/physics_tests.sh
      - run: ruff check .
      - run: mkdocs build --strict

FILE: .gitignore
Kind: text
Size: 210
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.so
.mypy_cache/
.pytest_cache/
.cache/

# Packaging
build/
dist/
*.egg-info/

# Environments
.venv/
.env/

# Editors
.idea/
.vscode/

# Telemetry output
telemetry/

FILE: CHANGELOG.md
Kind: text
Size: 192
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Changelog

## [0.1.0] - 2024-01-01
- Initial enterprise cockpit scaffold.
- Typer CLI, Textual TUI stubs, FastAPI server skeleton.
- Documentation suite, CI/CD, and packaging configuration.

FILE: CODE_OF_CONDUCT.md
Kind: text
Size: 350
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Code of Conduct

BLUX Commander follows the [Contributor Covenant](https://www.contributor-covenant.org/).

- Be respectful and inclusive.
- Provide constructive feedback.
- Report unacceptable behavior to ops@blux.systems.

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting
the project maintainers.

FILE: COMMERCIAL.md
Kind: text
Size: 740
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Commercial Licensing

BLUX Commander is dual-licensed. Open-source use is permitted under the Apache License 2.0. If you
plan to use the software for commercial purposes, you must obtain a commercial license.

## When a commercial license is required
- Embedding BLUX Commander into a paid or revenue-generating product or platform.
- Offering BLUX Commander as a hosted or managed service for customers.
- Integrating BLUX Commander into internal proprietary systems at scale or where redistribution is
  expected.
- Any other business use that goes beyond the permissions granted by the Apache License 2.0.

## How to obtain a commercial license
Email theoutervoid@outlook.com to discuss commercial terms and obtain written permission.

FILE: CONTRIBUTING.md
Kind: text
Size: 517
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Contributing

Thank you for considering a contribution to BLUX Commander!

## Development Environment

1. Create a virtual environment.
2. Install dependencies: `pip install -e .[dev]`.
3. Run `ruff`, `mypy`, and `pytest` before opening a pull request.

## Commit Guidelines

- Follow Conventional Commit semantics when possible.
- Include documentation updates for new features.
- Add tests for new modules or behaviors.

## Code of Conduct

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).

FILE: LICENSE
Kind: text
Size: 296
Last modified: 2026-01-21T18:01:44Z

CONTENT:
This project is dual-licensed.

- Open-source use is provided under the Apache License 2.0 in LICENSE-APACHE.
- Commercial and proprietary use requires a separate commercial license in LICENSE-COMMERCIAL.

See the README for details and contact theoutervoid@outlook.com for commercial licensing.

FILE: LICENSE-APACHE
Kind: text
Size: 11357
Last modified: 2026-01-21T18:01:44Z

CONTENT:
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

FILE: LICENSE-COMMERCIAL
Kind: text
Size: 1239
Last modified: 2026-01-21T18:01:44Z

CONTENT:
Proprietary Commercial License
Version 1.0

Copyright (c) 2024 BLUX. All rights reserved.

Permission is granted to use this software for internal evaluation and non-commercial purposes only.
Any commercial use, including without limitation embedding, distributing, hosting as a service,
or using within a paid or revenue-generating product, requires a separate written commercial
license from the copyright holder.

You may not modify, distribute, sublicense, rent, lease, lend, or otherwise make the software
available to any third party without prior written permission.

THE SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM,
OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This license terminates automatically upon breach. Upon termination, you must cease all use and
destroy all copies of the software.

To obtain a commercial license, contact: theoutervoid@outlook.com

FILE: NOTICE
Kind: text
Size: 142
Last modified: 2026-01-21T18:01:44Z

CONTENT:
BLUX Commander
Copyright (c) 2024 BLUX

This product includes software licensed under the Apache License 2.0. See LICENSE-APACHE for details.

FILE: README.md
Kind: text
Size: 4554
Last modified: 2026-01-22T05:15:43Z

CONTENT:
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

FILE: blux_commander/__init__.py
Kind: text
Size: 345
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""BLUX Commander package initialization."""

from importlib import metadata

__all__ = ["__version__"]

try:
    __version__ = metadata.version("blux-commander")
except metadata.PackageNotFoundError:  # pragma: no cover
    __version__ = "0.1.0"


def get_version() -> str:
    """Return the current package version."""

    return __version__

FILE: blux_commander/cli.py
Kind: text
Size: 2084
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Typer-based command line interface for BLUX Commander."""

from __future__ import annotations

import typer

from blux_commander.core import api, commander, plugins, telemetry, tui

app = typer.Typer(help="BLUX Commander — Unified Cockpit")
cmd_app = typer.Typer(help="Commander control surface")
app.add_typer(cmd_app, name="cmd")

plugins_app = typer.Typer(help="Plugin commands")
telemetry_app = typer.Typer(help="Telemetry commands")
ai_app = typer.Typer(help="AI console commands")

cmd_app.add_typer(plugins_app, name="plugins")
cmd_app.add_typer(telemetry_app, name="telemetry")
cmd_app.add_typer(ai_app, name="ai")

commander.bootstrap()


@cmd_app.command()
def dashboard() -> None:
    """Launch the Textual dashboard."""

    tui.launch_dashboard()


@cmd_app.command()
def status(verbose: bool = typer.Option(False, "--verbose", help="Show extended diagnostics")) -> None:
    """Print commander status."""

    commander.print_status(verbose=verbose)


@plugins_app.command("list")
def plugins_list(verbose: bool = typer.Option(False, "--verbose", help="Show discovery paths")) -> None:
    """List registered plugins."""

    plugins.list_registered(verbose=verbose)


@telemetry_app.command("tail")
def telemetry_tail(limit: int = typer.Option(10, help="Number of telemetry entries to show")) -> None:
    """Tail telemetry entries."""

    telemetry.tail(limit=limit)


@ai_app.command()
def ai(reflect: bool = typer.Option(False, "--reflect", help="Enable reflection mode")) -> None:
    """Interact with the AI developer console."""

    if reflect:
        print("Reflection mode activated. Awaiting conscious-agent guidance.")
    else:
        print("AI console ready. Use --reflect for guidance mode.")


@app.command()
def api_server(host: str = "127.0.0.1", port: int = 8000, reload: bool = False) -> None:
    """Run the FastAPI server."""

    api.run(host=host, port=port, reload=reload)


def get_app() -> typer.Typer:
    """Return the Typer app for entry-point exposure."""

    return app


if __name__ == "__main__":  # pragma: no cover
    app()

FILE: blux_commander/core/api.py
Kind: text
Size: 1501
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""FastAPI service exposing commander observability."""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from prometheus_client import CONTENT_TYPE_LATEST, CollectorRegistry, Gauge, generate_latest
import uvicorn

from blux_commander.core import commander

app = FastAPI(title="BLUX Commander API")
_registry = CollectorRegistry()
_commander_status = Gauge("blux_commander_subsystems", "Subsystem states", ["name"], registry=_registry)


@app.on_event("startup")
async def startup() -> None:
    """Initialize commander state on startup."""

    commander.bootstrap()
    for name, status in commander.state.subsystems.items():
        _commander_status.labels(name=name).set(1 if status == "connected" else 0)


@app.get("/health")
async def health() -> dict[str, str]:
    """Return service health."""

    return {"status": "ok"}


@app.get("/status")
async def status() -> dict[str, dict[str, str]]:
    """Return subsystem status."""

    return {"subsystems": commander.state.subsystems}


@app.get("/metrics")
async def metrics() -> JSONResponse:
    """Expose Prometheus metrics."""

    payload = generate_latest(_registry)
    return JSONResponse(content=payload.decode("utf-8"), media_type=CONTENT_TYPE_LATEST)


def run(host: str = "127.0.0.1", port: int = 8000, reload: bool = False) -> None:
    """Run the API using uvicorn."""

    uvicorn.run("blux_commander.core.api:app", host=host, port=port, reload=reload)  # noqa: S104

FILE: blux_commander/core/commander.py
Kind: text
Size: 2038
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Core orchestration hub for BLUX Commander."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List


@dataclass
class CommanderState:
    """Mutable runtime context shared across modules."""

    subsystems: Dict[str, str] = field(default_factory=dict)
    workflows: List[str] = field(default_factory=list)
    event_handlers: Dict[str, List[Callable[[Any], None]]] = field(default_factory=dict)


state = CommanderState()


def register_subsystem(name: str, status: str) -> None:
    """Register a subsystem status entry."""

    state.subsystems[name] = status


def add_workflow(name: str) -> None:
    """Record a workflow chain in the commander state."""

    state.workflows.append(name)


def subscribe(event: str, handler: Callable[[Any], None]) -> None:
    """Register an event handler for the given event."""

    state.event_handlers.setdefault(event, []).append(handler)


def publish(event: str, payload: Any) -> None:
    """Publish an event to all subscribers."""

    for handler in state.event_handlers.get(event, []):
        handler(payload)


def print_status(*, verbose: bool = False) -> None:
    """Print the current commander status to stdout."""

    header = "BLUX Commander Status"
    print(header)
    print("-" * len(header))
    for subsystem, status in sorted(state.subsystems.items()):
        print(f"{subsystem}: {status}")
    if verbose:
        print("\nRegistered workflows:")
        for workflow in state.workflows:
            print(f" - {workflow}")
        print("\nEvent subscriptions:")
        for event, handlers in state.event_handlers.items():
            print(f" - {event}: {len(handlers)} handlers")


def bootstrap() -> None:
    """Initialize default subsystem entries."""

    register_subsystem("traces", "idle")
    register_subsystem("audits", "idle")
    register_subsystem("execution_manifest", "pending")
    register_subsystem("guard_receipt", "pending")
    register_subsystem("envelope", "queued")

FILE: blux_commander/core/config.py
Kind: text
Size: 1555
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Configuration management utilities."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict

import yaml

CONFIG_FILENAMES = ["config.yaml", "config.yml"]
USER_CONFIG_DIR = Path.home() / ".config" / "blux-commander"


def load_config() -> Dict[str, Any]:
    """Load configuration from environment, user config, and local files."""

    config: Dict[str, Any] = {}
    config.update(_load_user_config())
    config.update(_load_project_config())
    config.update(_load_env_overrides())
    return config


def _load_user_config() -> Dict[str, Any]:
    """Load configuration from the user directory."""

    for filename in CONFIG_FILENAMES:
        path = USER_CONFIG_DIR / filename
        if path.exists():
            return _read_yaml(path)
    return {}


def _load_project_config() -> Dict[str, Any]:
    """Load configuration from the current working directory."""

    cwd = Path.cwd()
    for filename in CONFIG_FILENAMES:
        path = cwd / filename
        if path.exists():
            return _read_yaml(path)
    return {}


def _load_env_overrides() -> Dict[str, Any]:
    """Load overrides from environment variables."""

    overrides: Dict[str, Any] = {}
    for key, value in os.environ.items():
        if key.startswith("BLUX_CMD_"):
            overrides[key.lower()] = value
    return overrides


def _read_yaml(path: Path) -> Dict[str, Any]:
    """Read YAML data from disk."""

    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}

FILE: blux_commander/core/plugins.py
Kind: text
Size: 934
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Plugin discovery and lifecycle management."""

from __future__ import annotations

import importlib
from importlib import metadata
from typing import Iterable, List

PLUGIN_NAMESPACE = "blux.plugins"


def list_registered(*, verbose: bool = False) -> List[str]:
    """List registered plugin entry points."""

    plugins = sorted(_discover_plugins())
    if plugins:
        print("Registered plugins:")
        for name in plugins:
            print(f" - {name}")
    else:
        print("No plugins registered.")
    if verbose:
        print("\nDiscovery namespace:", PLUGIN_NAMESPACE)
    return plugins


def load(name: str) -> object:
    """Load a plugin module by dotted path."""

    return importlib.import_module(name)


def _discover_plugins() -> Iterable[str]:
    """Discover available plugin modules."""

    for entry_point in metadata.entry_points().select(group=PLUGIN_NAMESPACE):
        yield entry_point.name

FILE: blux_commander/core/telemetry.py
Kind: text
Size: 1445
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Telemetry stubs for BLUX Commander."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Iterable

TELEMETRY_DIR = Path(os.environ.get("BLUX_CMD_HOME", Path.home() / ".config" / "blux-commander"))
TELEMETRY_FILE = TELEMETRY_DIR / "logs" / "telemetry.jsonl"


def record(event: dict[str, object]) -> None:
    """Record a telemetry event to the JSONL file."""

    if os.environ.get("BLUX_CMD_TELEMETRY", "on").lower() == "off":
        return
    TELEMETRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with TELEMETRY_FILE.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def tail(limit: int = 10) -> None:
    """Print the last `limit` telemetry entries."""

    if not TELEMETRY_FILE.exists():
        print("No telemetry available yet.")
        return
    with TELEMETRY_FILE.open("r", encoding="utf-8") as handle:
        lines = handle.readlines()[-limit:]
    for line in lines:
        print(line.rstrip())


def load_history(limit: int | None = None) -> Iterable[dict[str, object]]:
    """Yield telemetry events up to the provided limit."""

    if not TELEMETRY_FILE.exists():
        return []
    with TELEMETRY_FILE.open("r", encoding="utf-8") as handle:
        for index, line in enumerate(handle):
            if limit is not None and index >= limit:
                break
            yield json.loads(line)

FILE: blux_commander/core/terminal.py
Kind: text
Size: 615
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Read-only terminal stubs for BLUX Commander."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def start_interactive(commands: Iterable[str] | None = None) -> None:
    """Reject interactive terminal sessions in read-only mode."""

    raise RuntimeError("Interactive terminal sessions are disabled in the read-only observability cockpit.")


def run_command(command: str, *, cwd: str | Path | None = None) -> None:
    """Reject command execution in read-only mode."""

    raise RuntimeError("Command execution is disabled in the read-only observability cockpit.")

FILE: blux_commander/core/tui.py
Kind: text
Size: 1369
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Textual dashboard launcher."""

from __future__ import annotations

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, Static

from blux_commander.ui.panels.ai_panel import AIPanel
from blux_commander.ui.panels.logs_panel import LogsPanel
from blux_commander.ui.panels.plugins_panel import PluginsPanel
from blux_commander.ui.panels.telemetry_panel import TelemetryPanel
from blux_commander.ui.panels.terminal_panel import TerminalPanel


class CommanderDashboard(App[None]):
    """Main Textual application for the BLUX Commander cockpit."""

    CSS_PATH = "ui/themes/default.tcss"
    TITLE = "BLUX Commander"

    def compose(self) -> ComposeResult:
        """Compose the dashboard layout."""

        yield Header(show_clock=True)
        with Container(id="cockpit"):
            yield PluginsPanel(id="plugins")
            yield TerminalPanel(id="terminal")
            with Container(id="right"):
                yield LogsPanel(id="logs")
                yield TelemetryPanel(id="telemetry")
                yield AIPanel(id="ai")
        yield Footer()
        yield Static("Reflection: Coordination is the art of giving every part its voice.", id="reflection")


def launch_dashboard() -> None:
    """Run the Textual dashboard application."""

    CommanderDashboard().run()

FILE: blux_commander/integrations/ca.py
Kind: text
Size: 243
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""cA integration stub."""

from __future__ import annotations

from blux_commander.core import commander


def register() -> None:
    """Register the cA integration with the commander."""

    commander.register_subsystem("ca", "listening")

FILE: blux_commander/integrations/doctrine.py
Kind: text
Size: 256
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Doctrine integration stub."""

from __future__ import annotations

from blux_commander.core import commander


def register() -> None:
    """Register the Doctrine integration with the commander."""

    commander.register_subsystem("doctrine", "idle")

FILE: blux_commander/integrations/quantum.py
Kind: text
Size: 258
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Quantum integration stub."""

from __future__ import annotations

from blux_commander.core import commander


def register() -> None:
    """Register the Quantum integration with the commander."""

    commander.register_subsystem("quantum", "connected")

FILE: blux_commander/ui/panels/ai_panel.py
Kind: text
Size: 280
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""AI panel widget."""

from __future__ import annotations

from textual.widgets import Static


class AIPanel(Static):
    """Provide AI reflection hints."""

    def on_mount(self) -> None:
        self.update("Reflection terminal ready. Awaiting prompts from cA integration.")

FILE: blux_commander/ui/panels/logs_panel.py
Kind: text
Size: 237
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Logs panel widget."""

from __future__ import annotations

from textual.widgets import Static


class LogsPanel(Static):
    """Display streaming logs."""

    def on_mount(self) -> None:
        self.update("Logs will appear here.")

FILE: blux_commander/ui/panels/plugins_panel.py
Kind: text
Size: 442
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Plugins panel widget."""

from __future__ import annotations

from textual.widgets import Static

from blux_commander.core import plugins


class PluginsPanel(Static):
    """Display available plugins."""

    def on_mount(self) -> None:
        plugin_list = plugins.list_registered()
        if plugin_list:
            lines = "\n".join(plugin_list)
        else:
            lines = "No plugins discovered."
        self.update(lines)

FILE: blux_commander/ui/panels/telemetry_panel.py
Kind: text
Size: 491
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Telemetry panel widget."""

from __future__ import annotations

from textual.widgets import Static

from blux_commander.core import telemetry


class TelemetryPanel(Static):
    """Display telemetry history."""

    def on_mount(self) -> None:
        entries = list(telemetry.load_history(limit=5))
        if not entries:
            self.update("No telemetry recorded.")
        else:
            rendered = "\n".join(str(entry) for entry in entries)
            self.update(rendered)

FILE: blux_commander/ui/panels/terminal_panel.py
Kind: text
Size: 395
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Terminal panel widget."""

from __future__ import annotations

from textual.widgets import Static


class TerminalPanel(Static):
    """Placeholder for the integrated terminal."""

    DEFAULT_CSS = """
    TerminalPanel {
        background: $surface-darken-2;
        padding: 1;
    }
    """

    def on_mount(self) -> None:
        self.update("Terminal ready. Read-only view enabled.")

FILE: blux_commander/ui/themes/default.tcss
Kind: text
Size: 224
Last modified: 2026-01-21T18:01:44Z

CONTENT:
#cockpit {
    layout: grid;
    grid-size: 1 2;
    grid-columns: 30% 70%;
}

#right {
    layout: vertical;
    height: 100%;
}

#reflection {
    dock: bottom;
    padding: 1;
    background: $accent;
    color: $text;
}

FILE: blux_commander/ui/themes/highcontrast.tcss
Kind: text
Size: 113
Last modified: 2026-01-21T18:01:44Z

CONTENT:
* {
    color: #ffffff;
    background: #000000;
}

#reflection {
    background: #ff00ff;
    color: #000000;
}

FILE: blux_commander/web/insights.py
Kind: text
Size: 4015
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Repository insights and dashboard aggregation utilities."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from .storage import StorageManager


@dataclass
class RepoRecord:
    name: str
    path: str
    description: Optional[str] = None

    def as_dict(self) -> Dict[str, Optional[str]]:
        return {"name": self.name, "path": self.path, "description": self.description}


@dataclass
class RepoInsight:
    name: str
    path: str
    branch: str
    dirty: bool
    latest_commit: Optional[str]
    ahead_commits: Optional[int]
    size_bytes: Optional[int]
    tracked_files: Optional[int]
    description: Optional[str] = None

    def as_dict(self) -> Dict[str, Optional[str]]:
        return {
            "name": self.name,
            "path": self.path,
            "branch": self.branch,
            "dirty": self.dirty,
            "latest_commit": self.latest_commit,
            "ahead_commits": self.ahead_commits,
            "size_bytes": self.size_bytes,
            "tracked_files": self.tracked_files,
            "description": self.description,
        }


class RepoIndex:
    """Persist and collect insights for tracked repositories."""

    def __init__(self, storage: StorageManager) -> None:
        self.storage = storage

    # ------------------------------------------------------------------
    def list_records(self) -> List[RepoRecord]:
        records = []
        for item in self.storage.load_repos():
            records.append(RepoRecord(**item))
        return records

    def upsert_record(self, record: RepoRecord) -> None:
        existing = {rec.name: rec for rec in self.list_records()}
        existing[record.name] = record
        self.storage.save_repos(rec.as_dict() for rec in existing.values())

    def remove_record(self, name: str) -> None:
        remaining = [rec for rec in self.list_records() if rec.name != name]
        self.storage.save_repos(rec.as_dict() for rec in remaining)

    # ------------------------------------------------------------------
    def collect_insights(self) -> List[RepoInsight]:
        insights: List[RepoInsight] = []
        for record in self.list_records():
            path = Path(record.path).expanduser()
            insights.append(_inspect_repo(record, path))
        return insights


def _inspect_repo(record: RepoRecord, path: Path) -> RepoInsight:
    if not path.exists():
        return RepoInsight(
            name=record.name,
            path=str(path),
            branch="missing",
            dirty=False,
            latest_commit=None,
            ahead_commits=None,
            size_bytes=None,
            tracked_files=None,
            description=record.description,
        )

    branch = "untracked"
    dirty = False
    latest_commit = None
    ahead = None
    size_bytes = _estimate_size(path)
    tracked_files = _count_files(path)
    return RepoInsight(
        name=record.name,
        path=str(path),
        branch=branch,
        dirty=dirty,
        latest_commit=latest_commit,
        ahead_commits=ahead,
        size_bytes=size_bytes,
        tracked_files=tracked_files,
        description=record.description,
    )


def _estimate_size(path: Path, *, file_limit: int = 5000) -> Optional[int]:
    if not path.exists():
        return None
    total = 0
    counted = 0
    for root, _, files in os.walk(path):
        for file in files:
            try:
                total += (Path(root) / file).stat().st_size
            except OSError:
                continue
            counted += 1
            if counted >= file_limit:
                return total
    return total


def _count_files(path: Path, *, file_limit: int = 5000) -> Optional[int]:
    if not path.exists():
        return None
    counted = 0
    for _, _, files in os.walk(path):
        counted += len(files)
        if counted >= file_limit:
            return counted
    return counted

FILE: blux_commander/web/server.py
Kind: text
Size: 1260
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""BLUX Commander web dashboard server."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from blux_commander.core import commander, plugins

from .storage import default_storage_dir


BASE_DIR = default_storage_dir()

app = FastAPI(title="BLUX Commander Web Dashboard", version="0.2.0")
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")

INDEX_FILE = Path(__file__).parent / "templates" / "index.html"


@app.get("/", response_class=HTMLResponse)
async def index() -> HTMLResponse:
    if not INDEX_FILE.exists():
        raise HTTPException(status_code=500, detail="Dashboard template missing")
    return HTMLResponse(INDEX_FILE.read_text(encoding="utf-8"))


@app.get("/api/status")
async def status() -> dict:
    return {
        "app": "blux-commander",
        "version": app.version,
        "cli_available": False,
        "config_dir": str(BASE_DIR),
        "subsystems": commander.state.subsystems,
    }


@app.get("/api/plugins")
async def list_plugins() -> dict:
    discovered = plugins.list_registered(verbose=False)
    return {"plugins": discovered}

FILE: blux_commander/web/static/app.js
Kind: text
Size: 5296
Last modified: 2026-01-21T18:01:44Z

CONTENT:
import React, { useEffect, useMemo, useState } from "https://esm.sh/react@18.3.1";
import { createRoot } from "https://esm.sh/react-dom@18.3.1/client";

const h = React.createElement;
const API_BASE = `${window.location.origin}/api`;

const ARTIFACT_TYPES = [
  {
    name: "envelope",
    summary: "Serialized payload envelopes emitted by upstream subsystems.",
  },
  {
    name: "guard_receipt",
    summary: "Guard receipts emitted by upstream audit pipelines.",
  },
  {
    name: "execution_manifest",
    summary: "Execution manifests generated by external orchestration layers.",
  },
  {
    name: "audits",
    summary: "Audit and log bundles published by external systems.",
  },
];

function SectionCard({ title, description, children }) {
  return h(
    "section",
    { className: "rounded-xl border border-slate-800 bg-slate-900/60 p-6 shadow-lg shadow-slate-950/40" },
    h(
      "div",
      { className: "mb-4 flex flex-col gap-2 md:flex-row md:items-center md:justify-between" },
      h("div", {}, h("h2", { className: "text-xl font-semibold" }, title), description && h("p", { className: "text-sm text-slate-400" }, description)),
    ),
    children,
  );
}

function useApi(path, fallback) {
  const [state, setState] = useState({ loading: true, data: fallback, error: null });

  useEffect(() => {
    let active = true;
    fetch(`${API_BASE}${path}`)
      .then((resp) => resp.json())
      .then((data) => {
        if (active) setState({ loading: false, data, error: null });
      })
      .catch((error) => {
        console.error("Failed to load", path, error);
        if (active) setState({ loading: false, data: fallback, error });
      });
    return () => {
      active = false;
    };
  }, [path, fallback]);

  return state;
}

function StatusSummary({ status }) {
  if (status.loading) {
    return h("p", { className: "text-sm text-slate-400" }, "Loading status...");
  }
  if (status.error) {
    return h("p", { className: "text-sm text-rose-300" }, "Status unavailable.");
  }

  return h(
    "div",
    { className: "grid gap-3 text-sm text-slate-300 md:grid-cols-2" },
    h("div", {}, h("span", { className: "text-slate-500" }, "Version"), h("div", { className: "font-medium" }, status.data.version)),
    h("div", {}, h("span", { className: "text-slate-500" }, "Config directory"), h("div", { className: "font-medium" }, status.data.config_dir)),
  );
}

function ArtifactList() {
  const rows = useMemo(
    () =>
      ARTIFACT_TYPES.map((artifact) =>
        h(
          "div",
          { key: artifact.name, className: "rounded-lg border border-slate-800 bg-slate-950/60 p-4" },
          h("p", { className: "text-sm font-semibold text-slate-200" }, artifact.name),
          h("p", { className: "mt-1 text-xs text-slate-400" }, artifact.summary),
        ),
      ),
    [],
  );
  return h("div", { className: "grid gap-3 md:grid-cols-2" }, rows);
}

function PluginList({ plugins }) {
  if (plugins.loading) {
    return h("p", { className: "text-sm text-slate-400" }, "Loading plugins...");
  }
  if (plugins.error) {
    return h("p", { className: "text-sm text-rose-300" }, "Plugin inventory unavailable.");
  }
  if (!plugins.data.plugins || plugins.data.plugins.length === 0) {
    return h("p", { className: "text-sm text-slate-400" }, "No plugins registered.");
  }
  return h(
    "ul",
    { className: "flex flex-col gap-2 text-sm text-slate-300" },
    plugins.data.plugins.map((plugin) =>
      h(
        "li",
        { key: plugin.name || plugin.path, className: "rounded-lg border border-slate-800 bg-slate-950/60 p-3" },
        h("p", { className: "font-medium" }, plugin.name || "Unnamed plugin"),
        plugin.path && h("p", { className: "text-xs text-slate-500" }, plugin.path),
      ),
    ),
  );
}

function App() {
  const status = useApi("/status", {});
  const plugins = useApi("/plugins", { plugins: [] });

  return h(
    "div",
    { className: "min-h-screen bg-slate-950 text-slate-100" },
    h(
      "main",
      { className: "mx-auto flex w-full max-w-6xl flex-col gap-6 px-6 py-10" },
      h(
        "header",
        { className: "flex flex-col gap-3" },
        h("p", { className: "text-xs font-semibold uppercase tracking-[0.3em] text-slate-500" }, "BLUX Commander"),
        h("h1", { className: "text-3xl font-semibold" }, "Read-only observability cockpit"),
        h(
          "p",
          { className: "max-w-2xl text-sm text-slate-400" },
          "Commander surfaces observability artifacts produced by other systems. It does not generate artifacts or perform actions.",
        ),
      ),
      h(
        SectionCard,
        {
          title: "Status",
          description: "Live health summary from the read-only cockpit.",
        },
        h(StatusSummary, { status }),
      ),
      h(
        SectionCard,
        {
          title: "Artifact inventory",
          description: "Artifact categories rendered by the cockpit.",
        },
        h(ArtifactList),
      ),
      h(
        SectionCard,
        {
          title: "Plugins",
          description: "Registered read-only integrations and views.",
        },
        h(PluginList, { plugins }),
      ),
    ),
  );
}

const root = createRoot(document.getElementById("root"));
root.render(h(App));

FILE: blux_commander/web/static/assets/style.css
Kind: text
Size: 3353
Last modified: 2026-01-21T18:01:44Z

CONTENT:
:root {
  color-scheme: dark;
  font-family: "Inter", "Segoe UI", system-ui, sans-serif;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  padding: 2rem;
  background: #0f1115;
  color: #f5f5f5;
}

a {
  color: #6dd3ff;
}

main.app {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.hero {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(0, 1fr);
  gap: 2rem;
  align-items: start;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.2em;
  color: #6dd3ff;
  font-size: 0.75rem;
  margin: 0 0 0.5rem;
}

h1 {
  margin: 0 0 0.75rem;
  font-size: 2.5rem;
}

.subtitle {
  margin: 0;
  color: #cbd2e5;
  line-height: 1.5;
}

.status {
  background: rgba(255, 255, 255, 0.05);
  padding: 1rem;
  border-radius: 0.75rem;
}

.status ul {
  list-style: none;
  padding: 0;
  margin: 0.75rem 0 0;
  display: grid;
  gap: 0.35rem;
}

section.panel {
  background: rgba(255, 255, 255, 0.05);
  padding: 1.5rem;
  border-radius: 0.75rem;
}

section.panel h2 {
  margin-top: 0;
}

.controls p {
  margin: 0.5rem 0 0;
  color: #cbd2e5;
}

.control-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.5rem;
  margin-top: 1rem;
}

.file-input {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  border: 1px dashed #6dd3ff;
  padding: 1rem;
  border-radius: 0.75rem;
  text-align: center;
  cursor: pointer;
}

.file-input input {
  display: none;
}

.file-input span {
  font-weight: 600;
}

.filter label {
  display: flex;
  flex-direction: column;
  font-weight: 600;
  margin-bottom: 0.35rem;
}

.filter input {
  width: 100%;
  padding: 0.6rem 0.75rem;
  border-radius: 0.5rem;
  border: 1px solid #2a2f3a;
  background: #141821;
  color: #f5f5f5;
}

.filter small {
  display: inline-flex;
  margin-top: 0.5rem;
  color: #9da7bc;
}

.actions {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

button {
  border: none;
  border-radius: 0.5rem;
  padding: 0.65rem 1rem;
  font-weight: 600;
  background: #6dd3ff;
  color: #0f1115;
  cursor: pointer;
}

button:disabled {
  background: #2a2f3a;
  color: #9da7bc;
  cursor: not-allowed;
}

.hint {
  margin: 0;
  color: #9da7bc;
  font-size: 0.85rem;
}

.load-status {
  margin-top: 1rem;
  padding: 0.75rem 1rem;
  border-radius: 0.5rem;
  background: #141821;
  color: #cbd2e5;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.summary-card {
  background: #141821;
  padding: 1rem;
  border-radius: 0.75rem;
}

.summary-card p {
  font-size: 1.75rem;
  margin: 0.5rem 0 0;
}

.empty-state {
  padding: 1rem;
  border-radius: 0.75rem;
  background: #141821;
  color: #9da7bc;
}

.card-list {
  display: grid;
  gap: 1rem;
}

.card {
  background: #141821;
  border-radius: 0.75rem;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.card-heading {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  align-items: baseline;
}

.card-heading h3 {
  margin: 0;
}

.card-heading span {
  color: #9da7bc;
  font-size: 0.85rem;
}

pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  font-size: 0.85rem;
  color: #cbd2e5;
}

@media (max-width: 900px) {
  body {
    padding: 1.25rem;
  }

  .hero {
    grid-template-columns: 1fr;
  }
}

FILE: blux_commander/web/storage.py
Kind: text
Size: 3911
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Local-first storage helpers for the BLUX Commander dashboard."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


_CONFIG_ENV_VAR = "BLUX_COMMANDER_HOME"
_DEFAULT_CONFIG_SUBDIR = Path(".config") / "blux-commander"


def default_storage_dir() -> Path:
    """Return the configured storage directory without creating it."""

    override = os.environ.get(_CONFIG_ENV_VAR)
    if override:
        path = Path(override).expanduser()
    else:
        path = Path.home() / _DEFAULT_CONFIG_SUBDIR
    return path


@dataclass
class CommandMemoryEntry:
    """In-memory representation of a recorded command execution."""

    command: str
    repo: Optional[str]
    exit_code: int
    output: List[str]
    error: List[str]
    timestamp: str
    duration_seconds: float

    def as_dict(self) -> Dict[str, Any]:
        return {
            "command": self.command,
            "repo": self.repo,
            "exit_code": self.exit_code,
            "output": self.output,
            "error": self.error,
            "timestamp": self.timestamp,
            "duration_seconds": self.duration_seconds,
        }


class StorageManager:
    """Persist command logs, memory, and auxiliary dashboard state."""

    def __init__(self, base_dir: Optional[Path] = None, *, memory_retention: int = 200) -> None:
        self.base_dir = base_dir or default_storage_dir()
        self.logs_dir = self.base_dir / "logs"
        self._memory_retention = memory_retention
        self._memory_entries: List[Dict[str, Any]] = []
        self._repos: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # Memory persistence
    # ------------------------------------------------------------------
    def append_memory(self, entry: CommandMemoryEntry) -> None:
        self._memory_entries.append(entry.as_dict())
        self._memory_entries = self._memory_entries[-self._memory_retention :]

    def list_memory(self, *, limit: Optional[int] = 50) -> List[Dict[str, Any]]:
        data = list(reversed(self._memory_entries))
        if limit is not None:
            data = data[:limit]
        return data

    # ------------------------------------------------------------------
    # Logging helpers
    # ------------------------------------------------------------------
    def write_log(self, entry: CommandMemoryEntry) -> Path:
        slug = self._slugify(entry.command)[:64] or "command"
        timestamp = datetime.fromisoformat(entry.timestamp).strftime("%Y%m%d-%H%M%S")
        log_path = self.logs_dir / f"{timestamp}-{slug}.log"
        return log_path

    @staticmethod
    def _slugify(value: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9-_]+", "-", value.strip().lower())
        return slug.strip("-")

    # ------------------------------------------------------------------
    # Repo registry persistence
    # ------------------------------------------------------------------
    def load_repos(self) -> List[Dict[str, Any]]:
        return list(self._repos)

    def save_repos(self, records: Iterable[Dict[str, Any]]) -> None:
        self._repos = list(records)


def build_memory_entry(
    *,
    command: str,
    repo: Optional[str],
    exit_code: int,
    output: Iterable[str],
    error: Iterable[str],
    duration_seconds: float,
    timestamp: Optional[datetime] = None,
) -> CommandMemoryEntry:
    """Convenience helper to create a :class:`CommandMemoryEntry`."""

    ts = (timestamp or datetime.now(UTC)).isoformat(timespec="seconds")
    return CommandMemoryEntry(
        command=command,
        repo=repo,
        exit_code=exit_code,
        output=list(output),
        error=list(error),
        timestamp=ts,
        duration_seconds=duration_seconds,
    )

FILE: blux_commander/web/templates/index.html
Kind: text
Size: 1492
Last modified: 2026-01-21T18:01:44Z

CONTENT:
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>BLUX Commander Dashboard</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
    <script src="https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio"></script>
    <script>
      tailwind.config = {
        darkMode: 'class',
        theme: {
          extend: {
            fontFamily: {
              display: ['Space Grotesk', 'sans-serif'],
            },
            colors: {
              primary: {
                50: '#ecfdf5',
                100: '#d1fae5',
                200: '#a7f3d0',
                300: '#6ee7b7',
                400: '#34d399',
                500: '#10b981',
                600: '#059669',
                700: '#047857',
                800: '#065f46',
                900: '#064e3b',
              },
              slate: tailwind.colors.slate,
            },
          },
        },
      };
    </script>
    <link rel="stylesheet" href="/static/assets/style.css" />
  </head>
  <body class="bg-slate-950 text-slate-100 font-display">
    <div id="root" class="min-h-screen"></div>
    <script type="module" src="/static/app.js"></script>
  </body>
</html>

FILE: docs/API.md
Kind: text
Size: 615
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# API Reference

## CLI Commands

| Command | Description |
|---------|-------------|
| `bluxq cmd dashboard` | Launch the Textual cockpit. |
| `bluxq cmd status` | Display current subsystem status information. |
| `bluxq cmd plugins list` | List registered Commander plugins. |
| `bluxq cmd telemetry tail` | Tail telemetry events in real-time. |

## HTTP Endpoints

The FastAPI service exposes the following read-only endpoints:

- `GET /api/status` – returns subsystem status snapshot.
- `GET /api/plugins` – lists registered plugin metadata.

Refer to module docstrings for additional handler descriptions.

FILE: docs/ARCHITECTURE.md
Kind: text
Size: 1338
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Architecture

BLUX Commander is organized into modular layers that coordinate read-only observability,
presentation, and data feeds.

## Core Layer

- **Commander Hub (`blux_commander/core/commander.py`)** – Maintains runtime context for
  observability artifacts.
- **Terminal (`blux_commander/core/terminal.py`)** – Disabled placeholder that rejects execution.
- **TUI (`blux_commander/core/tui.py`)** – Exposes Textual-powered cockpit panes.
- **API (`blux_commander/core/api.py`)** – Hosts FastAPI services for read-only dashboards.
- **Telemetry (`blux_commander/core/telemetry.py`)** – Records metrics and audit trails.
- **Config (`blux_commander/core/config.py`)** – Loads configuration from env, user, and project.
- **Plugins (`blux_commander/core/plugins.py`)** – Discovers, validates, and activates plugins.

## Integration Layer

Subsystem adapters in `blux_commander/integrations/` expose read-only hooks that publish
observability artifacts into the core state.

## Presentation Layer

- **Textual UI** – Multi-pane layout containing logs, telemetry, and plugin views.
- **Web Dashboard** – Optional FastAPI + template powered read-only interface.

## Data Layer

Telemetry and audit logs are displayed for situational awareness. Data is presented as read-only
snapshots to avoid mutating system state.

FILE: docs/CONFIGURATION.md
Kind: text
Size: 602
Last modified: 2026-01-21T18:01:44Z

CONTENT:
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

FILE: docs/INSTALL.md
Kind: text
Size: 622
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Installation

## Requirements

- Python 3.9+
- Supported operating systems: Linux, macOS, Windows (PowerShell), WSL2, and Android Termux
- Optional: virtual environment manager such as `venv`, `virtualenv`, or `conda`

## Steps

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -e .[dev]
```

The editable install registers the `bluxq` command-line entry point.

## Verification

- `bluxq cmd status` – prints current subsystem status summary.
- `bluxq cmd dashboard` – launches the Textual cockpit.
- `pytest` – executes automated tests and plugin fixtures.

FILE: docs/INTEGRATIONS.md
Kind: text
Size: 801
Last modified: 2026-01-21T18:01:44Z

CONTENT:
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

FILE: docs/OPERATIONS.md
Kind: text
Size: 758
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Operations

## Commander CLI

Use `bluxq cmd` to access read-only views:

- `dashboard` – start the Textual cockpit.
- `status` – review subsystem heartbeat information.
- `plugins list` – enumerate registered plugin modules.
- `telemetry tail` – stream recent telemetry entries.

## Runtime Modes

1. **Local Operator** – run the cockpit on a workstation for observation.
2. **Headless Observer** – run the FastAPI service for remote read-only insights.
3. **Hybrid** – use the TUI as a front-end while the API serves dashboards.

## Read-Only Guardrails

Commander does not launch terminals, execute commands, or issue tokens. It only renders observability
artifacts such as envelope, guard_receipt, execution_manifest, audits, and traces.

FILE: docs/ROADMAP.md
Kind: text
Size: 682
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Roadmap

## v0.1 (Current)
- Project scaffolding and dependency management.
- Typer CLI entry point with core command stubs.
- Textual cockpit layout placeholders.
- FastAPI server skeleton and telemetry integration points.
- Initial documentation and CI pipelines.

## v0.2
- Implement full telemetry persistence and Prometheus metrics.
- Expand plugin framework with dynamic loading and lifecycle management.
- Integrate BLUX-Lite and BLUX-Guard workflows.

## v1.0
- Production-hardened sandboxing, policy enforcement, and self-aware reflection terminal.
- Enterprise SSO integration and advanced audit reporting.
- Release artifacts and documentation for managed deployments.

FILE: docs/ROLE.md
Kind: text
Size: 807
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# BLUX Commander Role

## Mission

BLUX Commander is a **read-only observability cockpit** for the BLUX ecosystem. It **is not a
control plane** and it performs **no execution**.

## Allowed artifacts (display-only)

BLUX Commander may only display and visualize the following artifacts:

- traces
- envelope
- guard_receipt
- execution_manifest
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

FILE: docs/SECURITY.md
Kind: text
Size: 635
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Security

BLUX Commander emphasizes safe-by-default observability.

## Principles

- **Least Privilege** – dashboards run without execution, enforcement, or token issuance.
- **Auditability** – telemetry trails surface audits and traces for review.
- **Isolation** – no terminal execution or subprocess invocation is permitted.
- **Integrity** – plugins are metadata-only and do not mutate system state.

## Hardening Checklist

1. Restrict dashboard deployment to read-only networks or VPCs.
2. Enable TLS termination for the FastAPI server when exposed over networks.
3. Monitor observability feeds for anomalous activity.

FILE: docs/THEMES.md
Kind: text
Size: 429
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Themes

The Textual cockpit supports multiple theme presets stored under `blux_commander/ui/themes/`.

## Default Theme
- Balanced contrast for daily operations.
- Highlights actionable widgets and alerts.

## High Contrast Theme
- Optimized for accessibility and low-light environments.
- Enlarged fonts and high visibility color palette.

To apply a theme, set `BLUX_CMD_THEME=highcontrast` or adjust the configuration file.

FILE: docs/TROUBLESHOOTING.md
Kind: text
Size: 682
Last modified: 2026-01-21T18:01:44Z

CONTENT:
# Troubleshooting

## Common Issues

### TUI Does Not Start
- Ensure Textual >= 0.62 is installed.
- Check that the terminal supports rich color output.

### Plugins Missing
- Verify plugin directories in `config.yaml` and environment variables.
- Run `bluxq cmd plugins list --verbose` to display discovery paths.

### Telemetry Failures
- Confirm the telemetry directory is writable.
- Disable telemetry temporarily with `BLUX_CMD_TELEMETRY=off` and check logs.

## Collecting Diagnostics

Run `bluxq cmd status --verbose` to output detailed subsystem state, then attach the generated
JSONL telemetry snippet found in `~/.config/blux-commander/logs/` when filing support tickets.

FILE: docs/index.md
Kind: text
Size: 1113
Last modified: 2026-01-22T05:15:43Z

CONTENT:
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

FILE: mkdocs.yml
Kind: text
Size: 775
Last modified: 2026-01-21T18:01:44Z

CONTENT:
site_name: BLUX Commander Docs
site_description: Enterprise developer cockpit for the BLUX ecosystem
repo_url: https://github.com/blux/blux-commander
nav:
  - Home: index.md
  - Architecture: ARCHITECTURE.md
  - Install: INSTALL.md
  - Operations: OPERATIONS.md
  - Security: SECURITY.md
  - Integrations: INTEGRATIONS.md
  - API: API.md
  - Configuration: CONFIGURATION.md
  - Telemetry & Troubleshooting:
      - Telemetry Themes: THEMES.md
      - Troubleshooting: TROUBLESHOOTING.md
  - Roadmap: ROADMAP.md
theme:
  name: material
  features:
    - navigation.sections
    - navigation.tracking
    - toc.integrate
plugins:
  - search
markdown_extensions:
  - admonition
  - toc:
      permalink: true
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight

FILE: pyproject.toml
Kind: text
Size: 1423
Last modified: 2026-01-21T18:01:44Z

CONTENT:
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "blux-commander"
version = "0.1.0"
description = "BLUX Commander — Developer & AI Orchestration Cockpit for the BLUX Ecosystem"
readme = "README.md"
requires-python = ">=3.9"
license = { text = "Apache-2.0" }
authors = [{ name = "BLUX", email = "ops@blux.systems" }]
keywords = ["cli", "tui", "ai", "developer-tools", "blux"]
classifiers = [
  "License :: OSI Approved :: Apache Software License",
  "Programming Language :: Python",
  "Programming Language :: Python :: 3",
  "Programming Language :: Python :: 3.9",
]

dependencies = [
  "typer>=0.12.3",
  "textual>=0.62.0",
  "rich>=13.7.0",
  "psutil>=5.9.8",
  "pyyaml>=6.0.1",
  "sqlite-utils>=3.36",
  "fastapi>=0.115.0",
  "uvicorn>=0.30.0",
  "prometheus-client>=0.20.0",
  "jinja2>=3.1.4",
]

[project.optional-dependencies]
dev = ["pytest", "mypy", "ruff", "mkdocs-material", "httpx>=0.27"]

[project.scripts]
bluxq = "blux_commander.cli:app"

[project.entry-points."blux.plugins"]
cmd = "blux_commander.cli:get_app"

[tool.pytest.ini_options]
minversion = "7.0"
addopts = "-ra"
testpaths = ["tests"]

[tool.ruff]
line-length = 100
target-version = "py39"

[tool.mypy]
python_version = "3.9"
strict = false
warn_return_any = true
warn_unused_configs = true

[tool.setuptools]
license-files = ["LICENSE", "LICENSE-APACHE", "LICENSE-COMMERCIAL", "NOTICE"]

FILE: scripts/build_docs.sh
Kind: text
Size: 61
Last modified: 2026-01-21T18:01:44Z

CONTENT:
#!/usr/bin/env bash
set -euo pipefail

mkdocs build --strict

FILE: scripts/gen_filetree.py
Kind: text
Size: 1154
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Generate a repository file tree."""

from __future__ import annotations

import argparse
from pathlib import Path

EXCLUDE = {".git", "__pycache__", ".mypy_cache", ".pytest_cache", "build", "dist"}


def build_tree(root: Path, prefix: str = "") -> list[str]:
    """Return formatted tree lines for the directory."""

    entries = sorted([entry for entry in root.iterdir() if entry.name not in EXCLUDE])
    lines: list[str] = []
    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "
        lines.append(f"{prefix}{connector}{entry.name}")
        if entry.is_dir():
            extension = "    " if index == len(entries) - 1 else "│   "
            lines.extend(build_tree(entry, prefix + extension))
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate repository file tree")
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root_path = Path(args.root).resolve()
    print(root_path.name)
    for line in build_tree(root_path):
        print(line)


if __name__ == "__main__":
    main()

FILE: scripts/physics_tests.sh
Kind: text
Size: 2293
Last modified: 2026-01-22T05:15:43Z

CONTENT:
#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
cd "$ROOT_DIR"

fail=0

report_error() {
  echo "ERROR: $1" >&2
  fail=1
}

code_dirs=()
for dir in blux_commander tests scripts src app packages lib; do
  if [[ -d "$dir" ]]; then
    code_dirs+=("$dir")
  fi
done

exec_pattern='\bsubprocess\b|os\.system|exec\(|\bpopen\b|shell=True|child_process'
control_plane_pattern='["'\'']/(dispatch|run|execute|apply|mutate|approve|deny|issue|verify)\b'
enforcement_pattern='\benforce\b|\ballow\b|\bblock\b|\bdeny\b|\bdecision\b|\bpolicy_engine\b|\bmoderation\b'
trust_pattern='\btoken\b|\bcapability_token\b|\bsignature\b|\bverify\b|\bkey_id\b|\brevocation\b'
sibling_role_pattern='\bblux_guard\b|\bblux_lite\b|\bblux_reg\b|doctrine\.engine|doctrine_engine'

if [[ "${#code_dirs[@]}" -gt 0 ]]; then
  if rg -n -S -i "$exec_pattern" --glob '!.git/**' --glob '!scripts/physics_tests.sh' "${code_dirs[@]}"; then
    report_error "Found command-execution primitives in code directories."
  fi

  if rg -n -S -i "$control_plane_pattern" --glob '!.git/**' --glob '!scripts/physics_tests.sh' "${code_dirs[@]}"; then
    report_error "Found control-plane verbs in code paths."
  fi

  if rg -n -S -i "$enforcement_pattern" --glob '!.git/**' "${code_dirs[@]}"; then
    report_error "Found enforcement or decision keywords in code directories."
  fi

  if rg -n -S -i "$trust_pattern" --glob '!.git/**' "${code_dirs[@]}"; then
    report_error "Found token or trust keywords in code directories."
  fi

  if rg -n -S -i "$sibling_role_pattern" --glob '!.git/**' "${code_dirs[@]}"; then
    report_error "Found sibling-role or doctrine engine identifiers in code directories."
  fi
fi

if find . -type f -name "*.schema.json" -not -path "./.git/*" -not -path "./tests/fixtures/*" -print -quit | grep -q .; then
  report_error "Found local copies of contract schemas (*.schema.json)."
fi

if find . -type f \( -path "*/engine/*" -o -path "*/runner/*" -o -path "*/executor/*" -o -path "*/sandbox/*" \) -not -path "./.git/*" -print -quit | grep -q .; then
  report_error "Found files under execution-oriented paths (engine/, runner/, executor/, sandbox/)."
fi

if [[ "$fail" -ne 0 ]]; then
  echo "Physics tests failed." >&2
  exit 1
fi

echo "Physics tests passed."

FILE: scripts/run_tui_demo.py
Kind: text
Size: 238
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Run the BLUX Commander TUI demo."""

from __future__ import annotations

from blux_commander.core import commander, tui


def main() -> None:
    commander.bootstrap()
    tui.launch_dashboard()


if __name__ == "__main__":
    main()

FILE: scripts/update_readme_filetree.py
Kind: text
Size: 892
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Update the README file tree section."""

from __future__ import annotations

import re
from pathlib import Path

from gen_filetree import build_tree

README_PATH = Path(__file__).resolve().parents[1] / "README.md"
MARKER_START = "<!-- FILETREE:BEGIN -->"
MARKER_END = "<!-- FILETREE:END -->"


def main() -> None:
    tree_lines = ["```text"]
    tree_lines.extend(build_tree(Path(__file__).resolve().parents[1]))
    tree_lines.append("```")
    tree_block = "\n".join(tree_lines)
    content = README_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{MARKER_START}.*?{MARKER_END}", re.DOTALL,
    )
    replacement = f"{MARKER_START}\n<details><summary><strong>Repository File Tree</strong></summary>\n\n{tree_block}\n\n</details>\n{MARKER_END}"
    README_PATH.write_text(pattern.sub(replacement, content), encoding="utf-8")


if __name__ == "__main__":
    main()

FILE: tests/test_cli.py
Kind: text
Size: 301
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Tests for CLI wiring."""

from typer.testing import CliRunner

from blux_commander import cli

runner = CliRunner()


def test_status_command_runs() -> None:
    result = runner.invoke(cli.app, ["cmd", "status"])
    assert result.exit_code == 0
    assert "BLUX Commander Status" in result.stdout

FILE: tests/test_plugins.py
Kind: text
Size: 198
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Tests for plugin discovery."""

from blux_commander.core import plugins


def test_plugins_list_returns_list() -> None:
    result = plugins.list_registered()
    assert isinstance(result, list)

FILE: tests/test_terminal.py
Kind: text
Size: 391
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Tests for terminal utilities."""

import pytest

from blux_commander.core import terminal


def test_terminal_rejects_interactive() -> None:
    with pytest.raises(RuntimeError, match="read-only"):
        terminal.start_interactive()


def test_terminal_rejects_command_execution() -> None:
    with pytest.raises(RuntimeError, match="read-only"):
        terminal.run_command("status")

FILE: tests/test_tui.py
Kind: text
Size: 172
Last modified: 2026-01-21T18:01:44Z

CONTENT:
"""Tests for TUI dashboard."""

from blux_commander.core import tui


def test_dashboard_class_title() -> None:
    assert tui.CommanderDashboard.TITLE == "BLUX Commander"

FILE: tests/test_web_dashboard.py
Kind: text
Size: 1161
Last modified: 2026-01-21T18:01:44Z

CONTENT:
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator

import pytest
from fastapi.testclient import TestClient


MODULES_TO_CLEAR = [
    "blux_commander.web.server",
    "blux_commander.web.storage",
    "blux_commander.web.insights",
]


@pytest.fixture()
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[TestClient]:
    config_dir = tmp_path / ".config" / "blux-commander"
    monkeypatch.setenv("BLUX_COMMANDER_HOME", str(config_dir))
    import importlib

    for module in MODULES_TO_CLEAR:
        sys.modules.pop(module, None)
    server = importlib.import_module("blux_commander.web.server")
    with TestClient(server.app) as test_client:
        yield test_client


def test_status_endpoint(client: TestClient) -> None:
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.json()
    assert data["app"] == "blux-commander"
    assert "subsystems" in data


def test_plugins_endpoint(client: TestClient) -> None:
    response = client.get("/api/plugins")
    assert response.status_code == 200
    assert "plugins" in response.json()

## 4) Workflow Inventory (index only)
- .github/workflows/ci.yml (triggers: pull_request, push)

## 5) Search Index (raw results)

subprocess:
none

os.system:
none

exec(:
none

spawn:
none

shell:
none

child_process:
none

policy:
none

ethic:
none

enforce:
none

guard:
none

receipt:
none

token:
none

signature:
none

verify:
none

capability:
none

key_id:
none

contract:
none

schema:
none

$schema:
none

json-schema:
none

router:
none

orchestr:
none

execute:
none

command:
none

## 6) Notes
none
