"""Roast Your Fridge: one line, one laugh.

Writes a single fixed roast line to /output/entry.txt.
Standard library only, fully deterministic: every run writes the
same bytes, so the two grading runs agree exactly.
"""

import os
import sys

LINE = "My fridge's vegetable drawer is where salads go to die quietly, three weeks after I bought them to become a better person."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_children(directory):
    """Remove stale files inside the output dir, never the dir itself."""
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)


def main():
    if not 1 <= len(LINE.encode("utf-8")) <= 200:
        raise SystemExit("roast line must be 1-200 characters")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_children(OUTPUT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
