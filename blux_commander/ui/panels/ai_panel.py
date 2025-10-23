"""AI panel widget."""

from __future__ import annotations

from textual.widgets import Static


class AIPanel(Static):
    """Provide AI reflection hints."""

    def on_mount(self) -> None:
        self.update("Reflection terminal ready. Awaiting prompts from cA integration.")
