"""Funniest One-Line Performance Review -- make.fun entry.

Reads the single review line from entry.txt next to this file and
writes it to the output directory for the judge.
"""

import os
from pathlib import Path

MAX_CHARS = 140


def validate_line(raw: str) -> str:
    """Return the single review line, rejecting blank, multi-line or long input."""
    line = raw.strip()
    if not line:
        raise ValueError("entry.txt must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry.txt must hold exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} characters, over the {MAX_CHARS} limit")
    return line


def resolve_output_dir() -> Path:
    """Output directory from the environment, defaulting to /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_entry(line: str, output_dir: Path) -> Path:
    """Write the line with no trailing newline and verify it reads back identical."""
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(line, encoding="utf-8")
    if target.read_text(encoding="utf-8") != line:
        raise RuntimeError("written entry.txt did not read back identical")
    return target


def main() -> None:
    raw = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    line = validate_line(raw)
    write_entry(line, resolve_output_dir())
    print(line)


if __name__ == "__main__":
    main()
