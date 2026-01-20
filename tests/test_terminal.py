"""Tests for terminal utilities."""

import pytest

from blux_commander.core import terminal


def test_terminal_rejects_interactive() -> None:
    with pytest.raises(RuntimeError, match="read-only"):
        terminal.start_interactive()


def test_terminal_rejects_command_execution() -> None:
    with pytest.raises(RuntimeError, match="read-only"):
        terminal.run_command("status")
