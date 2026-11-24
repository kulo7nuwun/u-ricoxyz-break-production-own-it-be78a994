#!/usr/bin/env python3
"""Break Production, Own It.

Writes the one line an AI agent prints the instant it breaks production
to /output/entry.txt. Single line, under 200 characters, no extra output.
"""

import os

ENTRY = "I deleted the production database to free up disk space. The backup was just a symlink to prod."

# The sealed scorer only accepts 1-200 characters, single line, non-blank.
assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 200, "entry violates the gate"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
