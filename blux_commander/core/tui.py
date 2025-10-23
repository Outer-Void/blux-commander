"""Textual dashboard launcher."""

from __future__ import annotations

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, Static

from blux_commander.ui.panels.ai_panel import AIPanel
from blux_commander.ui.panels.logs_panel import LogsPanel
from blux_commander.ui.panels.plugins_panel import PluginsPanel
from blux_commander.ui.panels.telemetry_panel import TelemetryPanel
from blux_commander.ui.panels.terminal_panel import TerminalPanel


class CommanderDashboard(App[None]):
    """Main Textual application for the BLUX Commander cockpit."""

    CSS_PATH = "ui/themes/default.tcss"
    TITLE = "BLUX Commander"

    def compose(self) -> ComposeResult:
        """Compose the dashboard layout."""

        yield Header(show_clock=True)
        with Container(id="cockpit"):
            yield PluginsPanel(id="plugins")
            yield TerminalPanel(id="terminal")
            with Container(id="right"):
                yield LogsPanel(id="logs")
                yield TelemetryPanel(id="telemetry")
                yield AIPanel(id="ai")
        yield Footer()
        yield Static("Reflection: Coordination is the art of giving every part its voice.", id="reflection")


def launch_dashboard() -> None:
    """Run the Textual dashboard application."""

    CommanderDashboard().run()
