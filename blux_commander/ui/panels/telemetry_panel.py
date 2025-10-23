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
