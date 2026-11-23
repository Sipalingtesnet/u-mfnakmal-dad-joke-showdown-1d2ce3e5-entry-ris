#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes exactly one dad joke to /output/entry.txt. The joke is a fixed
string literal below; the program is deterministic, uses only the
standard library, and makes no network calls. Before writing it
self-checks the competition gate: the text must be 1-200 Unicode code
points, not only whitespace, and contain no newline characters.
"""

import os
import sys

# The chosen dad joke. The pun turns on "pressing": ironing a shirt
# hard, then "pressing charges" in the legal sense. "hard" makes the
# physical pressing action salient so the pun lands on first read.
JOKE = "I ironed my shirt so hard it filed a complaint — it said I was pressing charges."


def main() -> int:
    """Validate the joke and write it to /output/entry.txt."""
    # Gate checks: non-empty, not only whitespace, one line, 1-200 chars.
    if not JOKE:
        print("error: joke is empty", file=sys.stderr)
        return 1
    if JOKE.isspace():
        print("error: joke is only whitespace", file=sys.stderr)
        return 1
    if "\n" in JOKE or "\r" in JOKE:
        print("error: joke contains a newline", file=sys.stderr)
        return 1
    if not (1 <= len(JOKE) <= 200):
        print("error: joke length out of 1-200 range", file=sys.stderr)
        return 1

    # Create the output directory if needed and write the joke.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())