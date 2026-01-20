"""Read-only command stubs for the dashboard."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import AsyncIterator, List, Optional

from .storage import StorageManager, build_memory_entry


@dataclass
class CommandResult:
    """Structured outcome of a command request."""

    command: str
    repo: Optional[str]
    exit_code: int
    output: List[str]
    error: List[str]
    duration_seconds: float

    def as_dict(self) -> dict:
        return {
            "command": self.command,
            "repo": self.repo,
            "exit_code": self.exit_code,
            "output": self.output,
            "error": self.error,
            "duration_seconds": self.duration_seconds,
        }


class CommandExecutor:
    """Reject command execution in read-only mode."""

    def __init__(self, storage: StorageManager) -> None:
        self.storage = storage
        self.cli_path: Optional[str] = None

    # ------------------------------------------------------------------
    def execute(self, command: str, repo: Optional[str] = None) -> CommandResult:
        start = time.perf_counter()
        message = "Command execution is disabled in the read-only observability cockpit."
        result = CommandResult(
            command=command,
            repo=repo,
            exit_code=501,
            output=[],
            error=[message],
            duration_seconds=time.perf_counter() - start,
        )
        self._record(result)
        return result

    async def stream(self, command: str, repo: Optional[str] = None) -> AsyncIterator[dict]:
        message = "Command execution is disabled in the read-only observability cockpit."
        result = CommandResult(
            command=command,
            repo=repo,
            exit_code=501,
            output=[],
            error=[message],
            duration_seconds=0.0,
        )
        self._record(result)
        yield {"type": "error", "message": message}
        yield {"type": "exit", "code": result.exit_code, "duration": result.duration_seconds}

    # ------------------------------------------------------------------
    def _record(self, result: CommandResult) -> None:
        entry = build_memory_entry(
            command=result.command,
            repo=result.repo,
            exit_code=result.exit_code,
            output=result.output,
            error=result.error,
            duration_seconds=result.duration_seconds,
        )
        self.storage.append_memory(entry)

