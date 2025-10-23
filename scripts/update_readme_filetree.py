"""Update the README file tree section."""

from __future__ import annotations

import re
from pathlib import Path

from gen_filetree import build_tree

README_PATH = Path(__file__).resolve().parents[1] / "README.md"
MARKER_START = "<!-- FILETREE:BEGIN -->"
MARKER_END = "<!-- FILETREE:END -->"


def main() -> None:
    tree_lines = ["```text"]
    tree_lines.extend(build_tree(Path(__file__).resolve().parents[1]))
    tree_lines.append("```")
    tree_block = "\n".join(tree_lines)
    content = README_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        rf"{MARKER_START}.*?{MARKER_END}", re.DOTALL,
    )
    replacement = f"{MARKER_START}\n<details><summary><strong>Repository File Tree</strong></summary>\n\n{tree_block}\n\n</details>\n{MARKER_END}"
    README_PATH.write_text(pattern.sub(replacement, content), encoding="utf-8")


if __name__ == "__main__":
    main()
