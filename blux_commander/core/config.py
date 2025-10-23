"""Configuration management utilities."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict

import yaml

CONFIG_FILENAMES = ["config.yaml", "config.yml"]
USER_CONFIG_DIR = Path.home() / ".config" / "blux-commander"


def load_config() -> Dict[str, Any]:
    """Load configuration from environment, user config, and local files."""

    config: Dict[str, Any] = {}
    config.update(_load_user_config())
    config.update(_load_project_config())
    config.update(_load_env_overrides())
    return config


def _load_user_config() -> Dict[str, Any]:
    """Load configuration from the user directory."""

    for filename in CONFIG_FILENAMES:
        path = USER_CONFIG_DIR / filename
        if path.exists():
            return _read_yaml(path)
    return {}


def _load_project_config() -> Dict[str, Any]:
    """Load configuration from the current working directory."""

    cwd = Path.cwd()
    for filename in CONFIG_FILENAMES:
        path = cwd / filename
        if path.exists():
            return _read_yaml(path)
    return {}


def _load_env_overrides() -> Dict[str, Any]:
    """Load overrides from environment variables."""

    overrides: Dict[str, Any] = {}
    for key, value in os.environ.items():
        if key.startswith("BLUX_CMD_"):
            overrides[key.lower()] = value
    return overrides


def _read_yaml(path: Path) -> Dict[str, Any]:
    """Read YAML data from disk."""

    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}
