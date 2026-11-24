#!/usr/bin/env python3
"""Entry for make.fun — "One Word, One Username, One Reward".

Writes the entrant's own make.fun username — one word, nothing else —
to the output entry file, exactly as the competition's gate requires.
"""

import os

# The entrant's genuine make.fun handle: one word, no spaces, no gloss.
ENTRY_TEXT = "firli-ariadi"

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return DEFAULT_OUTPUT_PATH


def check_gate(text: str) -> None:
    """Raise unless the text passes the competition gate:
    UTF-8 text of 1 to 30 characters, not only white space."""
    if not (1 <= len(text) <= 30):
        raise ValueError(f"entry must be 1-30 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")  # raises if not UTF-8 encodable


def main() -> None:
    check_gate(ENTRY_TEXT)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Read back and verify: the file on disk must be exactly the entry text.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY_TEXT:
        raise SystemExit(f"read-back mismatch: wrote {ENTRY_TEXT!r}, read {written!r}")
    check_gate(written)


if __name__ == "__main__":
    main()
