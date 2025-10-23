"""Reg integration stub."""

from __future__ import annotations

from blux_commander.core import commander


def register() -> None:
    """Register the Reg integration with the commander."""

    commander.register_subsystem("reg", "synchronized")
