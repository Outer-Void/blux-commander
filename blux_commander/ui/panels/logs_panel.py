"""Logs panel widget."""

from __future__ import annotations

from textual.widgets import Static


class LogsPanel(Static):
    """Display streaming logs."""

    def on_mount(self) -> None:
        self.update("Logs will appear here.")
