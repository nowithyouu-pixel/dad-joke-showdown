#!/usr/bin/env python3
"""Entry for make.fun's "Dad Joke Showdown" bounty.

Writes one dad joke (86 Unicode characters) to /output/entry.txt.
No network, no input, deterministic.
"""

import os

TEXT = (
    "I keep a pencil behind my ear so I can draw the line "
    "whenever the kids step out of it."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text must be 1-200 chars, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry text must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
