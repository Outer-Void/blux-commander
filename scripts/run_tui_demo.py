"""Run the BLUX Commander TUI demo."""

from __future__ import annotations

from blux_commander.core import commander, tui


def main() -> None:
    commander.bootstrap()
    tui.launch_dashboard()


if __name__ == "__main__":
    main()
