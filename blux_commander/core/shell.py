"""Read-only shell stubs for BLUX Commander."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def start_interactive(commands: Iterable[str] | None = None) -> None:
    """Reject interactive shells in read-only mode."""

    raise RuntimeError("Interactive shells are disabled in the read-only observability cockpit.")


def run_command(command: str, *, cwd: str | Path | None = None) -> None:
    """Reject command execution in read-only mode."""

    raise RuntimeError("Command execution is disabled in the read-only observability cockpit.")
