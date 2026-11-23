#!/usr/bin/env python3
"""Write one complete story in exactly six words to /output/entry.txt.

The story, in three beats carried by six words:
"Widow" implies the loss that came before, "remarried" is the new
life she built on top of it, and "First husband knocked tonight"
detonates that new life: the man she buried, in every sense that
mattered, is standing at her door on the night it can least be
borne. Why he was presumed gone, whether it is really him, and
who opens the door are left for the reader to fill in.
"""
import os

TEXT = "Widow remarried. First husband knocked tonight."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
