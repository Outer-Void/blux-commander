"""Tests for TUI dashboard."""

from blux_commander.core import tui


def test_dashboard_class_title() -> None:
    assert tui.CommanderDashboard.TITLE == "BLUX Commander"
