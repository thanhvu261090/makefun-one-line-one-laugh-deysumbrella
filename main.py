#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun bounty entry.

Holds one fixed funny line and writes it exactly as-is, with no
trailing newline, to /output/entry.txt. Stdlib only: the grader
installs nothing. The gate allows 1-140 UTF-8 characters, one line.
"""

import os

# The joke itself: 94 characters, one line, no trailing newline.
ENTRY_LINE = (
    "I asked my AI assistant to write me a joke, so it billed me "
    "$2 and submitted this one instead."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = ENTRY_LINE
    if not 1 <= len(line) <= 140:
        raise ValueError("entry must be 1-140 characters, got %d" % len(line))
    if line != line.strip() or "\n" in line:
        raise ValueError("entry must be a single line with no edge whitespace")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print("wrote %d chars to %s" % (len(line), OUTPUT_PATH))


if __name__ == "__main__":
    main()
