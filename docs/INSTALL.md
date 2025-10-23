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
