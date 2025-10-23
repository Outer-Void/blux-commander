"""Quantum integration stub."""

from __future__ import annotations

from blux_commander.core import commander


def register() -> None:
    """Register the Quantum integration with the commander."""

    commander.register_subsystem("quantum", "connected")
