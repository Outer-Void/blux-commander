"""Plugin discovery and lifecycle management."""

from __future__ import annotations

import importlib
from importlib import metadata
from typing import Iterable, List

PLUGIN_NAMESPACE = "blux.plugins"


def list_registered(*, verbose: bool = False) -> List[str]:
    """List registered plugin entry points."""

    plugins = sorted(_discover_plugins())
    if plugins:
        print("Registered plugins:")
        for name in plugins:
            print(f" - {name}")
    else:
        print("No plugins registered.")
    if verbose:
        print("\nDiscovery namespace:", PLUGIN_NAMESPACE)
    return plugins


def load(name: str) -> object:
    """Load a plugin module by dotted path."""

    return importlib.import_module(name)


def _discover_plugins() -> Iterable[str]:
    """Discover available plugin modules."""

    for entry_point in metadata.entry_points().select(group=PLUGIN_NAMESPACE):
        yield entry_point.name
