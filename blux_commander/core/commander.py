"""Core orchestration hub for BLUX Commander."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List


@dataclass
class CommanderState:
    """Mutable runtime context shared across modules."""

    subsystems: Dict[str, str] = field(default_factory=dict)
    workflows: List[str] = field(default_factory=list)
    event_handlers: Dict[str, List[Callable[[Any], None]]] = field(default_factory=dict)


state = CommanderState()


def register_subsystem(name: str, status: str) -> None:
    """Register a subsystem status entry."""

    state.subsystems[name] = status


def add_workflow(name: str) -> None:
    """Record a workflow chain in the commander state."""

    state.workflows.append(name)


def subscribe(event: str, handler: Callable[[Any], None]) -> None:
    """Register an event handler for the given event."""

    state.event_handlers.setdefault(event, []).append(handler)


def publish(event: str, payload: Any) -> None:
    """Publish an event to all subscribers."""

    for handler in state.event_handlers.get(event, []):
        handler(payload)


def print_status(*, verbose: bool = False) -> None:
    """Print the current commander status to stdout."""

    header = "BLUX Commander Status"
    print(header)
    print("-" * len(header))
    for subsystem, status in sorted(state.subsystems.items()):
        print(f"{subsystem}: {status}")
    if verbose:
        print("\nRegistered workflows:")
        for workflow in state.workflows:
            print(f" - {workflow}")
        print("\nEvent subscriptions:")
        for event, handlers in state.event_handlers.items():
            print(f" - {event}: {len(handlers)} handlers")


def bootstrap() -> None:
    """Initialize default subsystem entries."""

    register_subsystem("traces", "idle")
    register_subsystem("audits", "idle")
    register_subsystem("execution_manifest", "pending")
    register_subsystem("guard_receipt", "pending")
    register_subsystem("envelope", "queued")
