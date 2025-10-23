"""Tests for shell utilities."""

from blux_commander.core import shell


def test_filtered_env_keys() -> None:
    env = shell._filtered_env()  # type: ignore[attr-defined]
    assert "PATH" in env
    assert all(key in {"PATH", "HOME", "SHELL", "BLUX_CMD_VERBOSE"} for key in env)
