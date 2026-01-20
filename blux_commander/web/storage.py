"""Local-first storage helpers for the BLUX Commander dashboard."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


_CONFIG_ENV_VAR = "BLUX_COMMANDER_HOME"
_DEFAULT_CONFIG_SUBDIR = Path(".config") / "blux-commander"


def default_storage_dir() -> Path:
    """Return the configured storage directory without creating it."""

    override = os.environ.get(_CONFIG_ENV_VAR)
    if override:
        path = Path(override).expanduser()
    else:
        path = Path.home() / _DEFAULT_CONFIG_SUBDIR
    return path


@dataclass
class CommandMemoryEntry:
    """In-memory representation of a recorded command execution."""

    command: str
    repo: Optional[str]
    exit_code: int
    output: List[str]
    error: List[str]
    timestamp: str
    duration_seconds: float

    def as_dict(self) -> Dict[str, Any]:
        return {
            "command": self.command,
            "repo": self.repo,
            "exit_code": self.exit_code,
            "output": self.output,
            "error": self.error,
            "timestamp": self.timestamp,
            "duration_seconds": self.duration_seconds,
        }


class StorageManager:
    """Persist command logs, memory, and auxiliary dashboard state."""

    def __init__(self, base_dir: Optional[Path] = None, *, memory_retention: int = 200) -> None:
        self.base_dir = base_dir or default_storage_dir()
        self.logs_dir = self.base_dir / "logs"
        self._memory_retention = memory_retention
        self._memory_entries: List[Dict[str, Any]] = []
        self._repos: List[Dict[str, Any]] = []

    # ------------------------------------------------------------------
    # Memory persistence
    # ------------------------------------------------------------------
    def append_memory(self, entry: CommandMemoryEntry) -> None:
        self._memory_entries.append(entry.as_dict())
        self._memory_entries = self._memory_entries[-self._memory_retention :]

    def list_memory(self, *, limit: Optional[int] = 50) -> List[Dict[str, Any]]:
        data = list(reversed(self._memory_entries))
        if limit is not None:
            data = data[:limit]
        return data

    # ------------------------------------------------------------------
    # Logging helpers
    # ------------------------------------------------------------------
    def write_log(self, entry: CommandMemoryEntry) -> Path:
        slug = self._slugify(entry.command)[:64] or "command"
        timestamp = datetime.fromisoformat(entry.timestamp).strftime("%Y%m%d-%H%M%S")
        log_path = self.logs_dir / f"{timestamp}-{slug}.log"
        return log_path

    @staticmethod
    def _slugify(value: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9-_]+", "-", value.strip().lower())
        return slug.strip("-")

    # ------------------------------------------------------------------
    # Repo registry persistence
    # ------------------------------------------------------------------
    def load_repos(self) -> List[Dict[str, Any]]:
        return list(self._repos)

    def save_repos(self, records: Iterable[Dict[str, Any]]) -> None:
        self._repos = list(records)


def build_memory_entry(
    *,
    command: str,
    repo: Optional[str],
    exit_code: int,
    output: Iterable[str],
    error: Iterable[str],
    duration_seconds: float,
    timestamp: Optional[datetime] = None,
) -> CommandMemoryEntry:
    """Convenience helper to create a :class:`CommandMemoryEntry`."""

    ts = (timestamp or datetime.now(UTC)).isoformat(timespec="seconds")
    return CommandMemoryEntry(
        command=command,
        repo=repo,
        exit_code=exit_code,
        output=list(output),
        error=list(error),
        timestamp=ts,
        duration_seconds=duration_seconds,
    )
