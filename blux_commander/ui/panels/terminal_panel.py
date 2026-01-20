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
