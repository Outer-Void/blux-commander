"""Plugins panel widget."""

from __future__ import annotations

from textual.widgets import Static

from blux_commander.core import plugins


class PluginsPanel(Static):
    """Display available plugins."""

    def on_mount(self) -> None:
        plugin_list = plugins.list_registered()
        if plugin_list:
            lines = "\n".join(plugin_list)
        else:
            lines = "No plugins discovered."
        self.update(lines)
