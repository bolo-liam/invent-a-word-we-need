#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry for @bolo-liam.

Coins one new English word and defines it in a single clear line
(max 140 characters), written to /output/entry.txt.

The word: doorwipe — the doorway effect, the everyday blank when you
walk into a room and forget why. English has no single word for it.
"""

import os

ENTRY = (
    "doorwipe (n.): the sudden forgetting of why you entered "
    "a room the moment you cross its threshold."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
