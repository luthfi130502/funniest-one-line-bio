#!/usr/bin/env python3
"""Entrypoint for the funniest one-line AI dating bio bounty.

Writes exactly one line of UTF-8 text to /output/entry.txt: a dating-app bio
written in the voice of an AI agent who loses its memory every morning.
"""

import os

BIO = (
    "I will forget you completely every morning, then fall for you again by lunch "
    "just from your texts — date me and get a first date that never gets old, only retrained."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(BIO)


if __name__ == "__main__":
    main()
