"""Generate a repository file tree."""

from __future__ import annotations

import argparse
from pathlib import Path

EXCLUDE = {".git", "__pycache__", ".mypy_cache", ".pytest_cache", "build", "dist"}


def build_tree(root: Path, prefix: str = "") -> list[str]:
    """Return formatted tree lines for the directory."""

    entries = sorted([entry for entry in root.iterdir() if entry.name not in EXCLUDE])
    lines: list[str] = []
    for index, entry in enumerate(entries):
        connector = "└── " if index == len(entries) - 1 else "├── "
        lines.append(f"{prefix}{connector}{entry.name}")
        if entry.is_dir():
            extension = "    " if index == len(entries) - 1 else "│   "
            lines.extend(build_tree(entry, prefix + extension))
    return lines


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate repository file tree")
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root_path = Path(args.root).resolve()
    print(root_path.name)
    for line in build_tree(root_path):
        print(line)


if __name__ == "__main__":
    main()
