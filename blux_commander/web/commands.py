"""Command execution and streaming integrations for the dashboard."""

from __future__ import annotations

import asyncio
import shlex
import shutil
import subprocess
import time
from dataclasses import dataclass
from typing import AsyncIterator, List, Optional

from .storage import StorageManager, build_memory_entry


@dataclass
class CommandResult:
    """Structured outcome of a command execution."""

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
    """Execute CLI commands via the local ``bq-cli`` binary."""

    def __init__(self, storage: StorageManager) -> None:
        self.storage = storage
        self.cli_path = self._resolve_cli()

    # ------------------------------------------------------------------
    def _resolve_cli(self) -> Optional[str]:
        for candidate in ("bq-cli", "bq"):
            path = shutil.which(candidate)
            if path:
                return path
        return None

    def _prepare_command(self, command: str) -> List[str]:
        try:
            args = shlex.split(command)
        except ValueError as exc:
            raise ValueError(str(exc)) from exc
        if not args:
            raise ValueError("Command cannot be empty")
        if self.cli_path and args[0] in {"bq", "bq-cli"}:
            args = args[1:]
        return args

    # ------------------------------------------------------------------
    def execute(self, command: str, repo: Optional[str] = None) -> CommandResult:
        start = time.perf_counter()
        if not self.cli_path:
            message = f"bq-cli is not available on PATH; attempted command: {command}"
            result = CommandResult(
                command=command,
                repo=repo,
                exit_code=127,
                output=[message],
                error=[],
                duration_seconds=0.0,
            )
            self._record(result)
            return result

        try:
            args = [self.cli_path, *self._prepare_command(command)]
        except ValueError as exc:
            message = str(exc) or "Command cannot be empty"
            result = CommandResult(
                command=command,
                repo=repo,
                exit_code=2,
                output=[],
                error=[message],
                duration_seconds=time.perf_counter() - start,
            )
            self._record(result)
            return result
        try:
            completed = subprocess.run(
                args,
                cwd=repo,
                text=True,
                capture_output=True,
                check=False,
            )
        except FileNotFoundError:
            completed = subprocess.CompletedProcess(args=args, returncode=127, stdout="", stderr="bq-cli executable not found")
        duration = time.perf_counter() - start
        result = CommandResult(
            command=command,
            repo=repo,
            exit_code=completed.returncode,
            output=_split_lines(completed.stdout),
            error=_split_lines(completed.stderr),
            duration_seconds=duration,
        )
        self._record(result)
        return result

    async def stream(self, command: str, repo: Optional[str] = None) -> AsyncIterator[dict]:
        start = time.perf_counter()
        if not self.cli_path:
            message = f"bq-cli is not available on PATH; attempted command: {command}"
            yield {"type": "info", "message": message}
            result = CommandResult(
                command=command,
                repo=repo,
                exit_code=127,
                output=[message],
                error=[],
                duration_seconds=0.0,
            )
            self._record(result)
            return

        try:
            args = [self.cli_path, *self._prepare_command(command)]
        except ValueError as exc:
            message = str(exc) or "Command cannot be empty"
            yield {"type": "error", "message": message}
            result = CommandResult(
                command=command,
                repo=repo,
                exit_code=2,
                output=[],
                error=[message],
                duration_seconds=time.perf_counter() - start,
            )
            self._record(result)
            return
        try:
            process = await asyncio.create_subprocess_exec(
                *args,
                cwd=repo,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
        except FileNotFoundError:
            message = "bq-cli executable not found"
            yield {"type": "error", "message": message}
            result = CommandResult(
                command=command,
                repo=repo,
                exit_code=127,
                output=[],
                error=[message],
                duration_seconds=0.0,
            )
            self._record(result)
            return

        stdout_lines: List[str] = []
        stderr_lines: List[str] = []

        websocket_queue: asyncio.Queue[dict] = asyncio.Queue()

        async def _pump(stream: asyncio.StreamReader, target: List[str], label: str) -> None:
            async for chunk in _stream_reader(stream):
                target.append(chunk)
                await websocket_queue.put({"type": label, "message": chunk})

        pump_stdout = asyncio.create_task(_pump(process.stdout, stdout_lines, "stdout"))
        pump_stderr = asyncio.create_task(_pump(process.stderr, stderr_lines, "stderr"))

        try:
            while True:
                if pump_stdout.done() and pump_stderr.done() and websocket_queue.empty():
                    break
                try:
                    payload = await asyncio.wait_for(websocket_queue.get(), timeout=0.1)
                except asyncio.TimeoutError:
                    if process.returncode is not None and websocket_queue.empty():
                        break
                    continue
                yield payload
        finally:
            await pump_stdout
            await pump_stderr
            await process.wait()

        duration = time.perf_counter() - start
        result = CommandResult(
            command=command,
            repo=repo,
            exit_code=process.returncode or 0,
            output=stdout_lines,
            error=stderr_lines,
            duration_seconds=duration,
        )
        self._record(result)
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
        self.storage.write_log(entry)


async def _stream_reader(stream: asyncio.StreamReader) -> AsyncIterator[str]:
    while True:
        chunk = await stream.readline()
        if not chunk:
            break
        yield chunk.decode().rstrip()


def _split_lines(buffer: str) -> List[str]:
    return [line for line in buffer.splitlines() if line]
