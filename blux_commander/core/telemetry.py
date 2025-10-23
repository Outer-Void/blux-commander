"""Telemetry stubs for BLUX Commander."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Iterable

TELEMETRY_DIR = Path(os.environ.get("BLUX_CMD_HOME", Path.home() / ".config" / "blux-commander"))
TELEMETRY_FILE = TELEMETRY_DIR / "logs" / "telemetry.jsonl"


def record(event: dict[str, object]) -> None:
    """Record a telemetry event to the JSONL file."""

    if os.environ.get("BLUX_CMD_TELEMETRY", "on").lower() == "off":
        return
    TELEMETRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with TELEMETRY_FILE.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")


def tail(limit: int = 10) -> None:
    """Print the last `limit` telemetry entries."""

    if not TELEMETRY_FILE.exists():
        print("No telemetry available yet.")
        return
    with TELEMETRY_FILE.open("r", encoding="utf-8") as handle:
        lines = handle.readlines()[-limit:]
    for line in lines:
        print(line.rstrip())


def load_history(limit: int | None = None) -> Iterable[dict[str, object]]:
    """Yield telemetry events up to the provided limit."""

    if not TELEMETRY_FILE.exists():
        return []
    with TELEMETRY_FILE.open("r", encoding="utf-8") as handle:
        for index, line in enumerate(handle):
            if limit is not None and index >= limit:
                break
            yield json.loads(line)
