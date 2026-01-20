"""Repository insights and dashboard aggregation utilities."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from .storage import StorageManager


@dataclass
class RepoRecord:
    name: str
    path: str
    description: Optional[str] = None

    def as_dict(self) -> Dict[str, Optional[str]]:
        return {"name": self.name, "path": self.path, "description": self.description}


@dataclass
class RepoInsight:
    name: str
    path: str
    branch: str
    dirty: bool
    latest_commit: Optional[str]
    ahead_commits: Optional[int]
    size_bytes: Optional[int]
    tracked_files: Optional[int]
    description: Optional[str] = None

    def as_dict(self) -> Dict[str, Optional[str]]:
        return {
            "name": self.name,
            "path": self.path,
            "branch": self.branch,
            "dirty": self.dirty,
            "latest_commit": self.latest_commit,
            "ahead_commits": self.ahead_commits,
            "size_bytes": self.size_bytes,
            "tracked_files": self.tracked_files,
            "description": self.description,
        }


class RepoIndex:
    """Persist and collect insights for tracked repositories."""

    def __init__(self, storage: StorageManager) -> None:
        self.storage = storage

    # ------------------------------------------------------------------
    def list_records(self) -> List[RepoRecord]:
        records = []
        for item in self.storage.load_repos():
            records.append(RepoRecord(**item))
        return records

    def upsert_record(self, record: RepoRecord) -> None:
        existing = {rec.name: rec for rec in self.list_records()}
        existing[record.name] = record
        self.storage.save_repos(rec.as_dict() for rec in existing.values())

    def remove_record(self, name: str) -> None:
        remaining = [rec for rec in self.list_records() if rec.name != name]
        self.storage.save_repos(rec.as_dict() for rec in remaining)

    # ------------------------------------------------------------------
    def collect_insights(self) -> List[RepoInsight]:
        insights: List[RepoInsight] = []
        for record in self.list_records():
            path = Path(record.path).expanduser()
            insights.append(_inspect_repo(record, path))
        return insights


def _inspect_repo(record: RepoRecord, path: Path) -> RepoInsight:
    if not path.exists():
        return RepoInsight(
            name=record.name,
            path=str(path),
            branch="missing",
            dirty=False,
            latest_commit=None,
            ahead_commits=None,
            size_bytes=None,
            tracked_files=None,
            description=record.description,
        )

    branch = "untracked"
    dirty = False
    latest_commit = None
    ahead = None
    size_bytes = _estimate_size(path)
    tracked_files = _count_files(path)
    return RepoInsight(
        name=record.name,
        path=str(path),
        branch=branch,
        dirty=dirty,
        latest_commit=latest_commit,
        ahead_commits=ahead,
        size_bytes=size_bytes,
        tracked_files=tracked_files,
        description=record.description,
    )


def _estimate_size(path: Path, *, file_limit: int = 5000) -> Optional[int]:
    if not path.exists():
        return None
    total = 0
    counted = 0
    for root, _, files in os.walk(path):
        for file in files:
            try:
                total += (Path(root) / file).stat().st_size
            except OSError:
                continue
            counted += 1
            if counted >= file_limit:
                return total
    return total


def _count_files(path: Path, *, file_limit: int = 5000) -> Optional[int]:
    if not path.exists():
        return None
    counted = 0
    for _, _, files in os.walk(path):
        counted += len(files)
        if counted >= file_limit:
            return counted
    return counted
