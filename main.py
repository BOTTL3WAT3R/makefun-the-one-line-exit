#!/usr/bin/env python3
"""The One-Line Exit — a one-line resignation letter.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
The letter is from a fortune teller who resigns because she has seen
next quarter's numbers — and refuses to be the one who has to tell them.
"""

import os

ENTRY = (
    "I resign as your fortune teller, effective immediately — "
    "I've seen next quarter's numbers, and I refuse to be the one who has to tell you."
)


def main() -> None:
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} out of gate range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
