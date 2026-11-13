#!/usr/bin/env python3
"""ai-joke-03 entry (Python 3.13, standard library only).

The competition grades one fixed one-liner about AI coding agents. The
sandbox has no network and nothing is installed, so the joke ships as data
inside this file and the program writes it, byte for byte, to the output
file the judge reads: $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader,
/output/entry.txt in it. Writing fixed bytes makes both grader runs
identical by construction.

Gate: the file is UTF-8, 1 to 280 characters counted as Unicode code
points, at least one of them not white space, and no trailing line end --
the judge reads exactly the bytes written.
"""

import os
from pathlib import Path

JOKE = (
    'My coding agent keeps saying "it works on my machine" '
    "— which is awkward, because it is the machine."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
