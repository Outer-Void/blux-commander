"""Tests for plugin discovery."""

from blux_commander.core import plugins


def test_plugins_list_returns_list() -> None:
    result = plugins.list_registered()
    assert isinstance(result, list)
