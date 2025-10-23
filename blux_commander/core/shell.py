"""Interactive shell stubs for BLUX Commander."""

from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path
from typing import Iterable

DEFAULT_SHELL = os.environ.get("SHELL", "bash")


def start_interactive(commands: Iterable[str] | None = None) -> None:
    """Launch an interactive shell session or run provided commands."""

    if commands is None:
        _spawn_shell()
    else:
        for command in commands:
            run_command(command)


def _spawn_shell() -> None:
    """Start a subshell in the current working directory."""

    subprocess.call(DEFAULT_SHELL)  # noqa: S603, S607


def run_command(command: str, *, cwd: str | Path | None = None) -> subprocess.CompletedProcess[str]:
    """Execute a single command in a sandboxed subprocess."""

    args = shlex.split(command)
    result = subprocess.run(  # noqa: S603
        args,
        check=False,
        capture_output=True,
        text=True,
        cwd=cwd,
        env=_filtered_env(),
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    return result


def _filtered_env() -> dict[str, str]:
    """Return a sanitized copy of the current environment."""

    allowed = {"PATH", "HOME", "SHELL", "BLUX_CMD_VERBOSE"}
    return {key: value for key, value in os.environ.items() if key in allowed}
