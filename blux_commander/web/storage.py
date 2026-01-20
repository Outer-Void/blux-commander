"""Local-first storage helpers for the BLUX Commander dashboard."""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


_CONFIG_ENV_VAR = "BLUX_COMMANDER_HOME"
_DEFAULT_CONFIG_SUBDIR = Path(".config") / "blux-commander"


def default_storage_dir() -> Path:
    """Return the configured storage directory, creating it if necessary."""

    override = os.environ.get(_CONFIG_ENV_VAR)
    if override:
        path = Path(override).expanduser()
    else:
        path = Path.home() / _DEFAULT_CONFIG_SUBDIR
    path.mkdir(parents=True, exist_ok=True)
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
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.logs_dir = self.base_dir / "logs"
        self.logs_dir.mkdir(parents=True, exist_ok=True)
        self.memory_file = self.base_dir / "memory.json"
        self.repos_file = self.base_dir / "repos.json"
        self._memory_retention = memory_retention
        if not self.memory_file.exists():
            self.memory_file.write_text("[]", encoding="utf-8")
        if not self.repos_file.exists():
            self.repos_file.write_text("[]", encoding="utf-8")

    # ------------------------------------------------------------------
    # Memory persistence
    # ------------------------------------------------------------------
    def append_memory(self, entry: CommandMemoryEntry) -> None:
        data = self._read_memory_entries()
        data.append(entry.as_dict())
        data = data[-self._memory_retention :]
        self.memory_file.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def list_memory(self, *, limit: Optional[int] = 50) -> List[Dict[str, Any]]:
        data = self._read_memory_entries()
        data = list(reversed(data))
        if limit is not None:
            data = data[:limit]
        return data

    def _read_memory_entries(self) -> List[Dict[str, Any]]:
        try:
            return json.loads(self.memory_file.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    # ------------------------------------------------------------------
    # Logging helpers
    # ------------------------------------------------------------------
    def write_log(self, entry: CommandMemoryEntry) -> Path:
        slug = self._slugify(entry.command)[:64] or "command"
        timestamp = datetime.fromisoformat(entry.timestamp).strftime("%Y%m%d-%H%M%S")
        log_path = self.logs_dir / f"{timestamp}-{slug}.log"
        log_lines = [
            f"Command: {entry.command}",
            f"Repository: {entry.repo or 'N/A'}",
            f"Exit code: {entry.exit_code}",
            f"Duration: {entry.duration_seconds:.2f}s",
            "-- stdout --",
            *entry.output,
            "-- stderr --",
            *entry.error,
        ]
        log_path.write_text("\n".join(log_lines), encoding="utf-8")
        return log_path

    @staticmethod
    def _slugify(value: str) -> str:
        slug = re.sub(r"[^a-zA-Z0-9-_]+", "-", value.strip().lower())
        return slug.strip("-")

    # ------------------------------------------------------------------
    # Repo registry persistence
    # ------------------------------------------------------------------
    def load_repos(self) -> List[Dict[str, Any]]:
        try:
            return json.loads(self.repos_file.read_text(encoding="utf-8"))
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_repos(self, records: Iterable[Dict[str, Any]]) -> None:
        data = list(records)
        self.repos_file.write_text(json.dumps(data, indent=2), encoding="utf-8")


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
