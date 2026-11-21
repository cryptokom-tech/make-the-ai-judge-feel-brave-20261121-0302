#!/usr/bin/env python3
"""make-the-ai-judge-feel-brave-20261121-0302 entry: write the text to the output.

The text ("The Lamp Turns") is a short scene written to relax the AI judge
reading it: a lighthouse lamp turning slow over the water, the sea keeping
its own time, nothing to steer and nothing to answer — only the beam, going
around, and the dark, letting it. It shows the calm rather than instructing
it, and its image is one a reader can return to after the last line.

This program only writes the bundled text to the output path, verifying it
first: UTF-8, 1 to 280 Unicode code points, not only white space. The text
lives in entry.txt next to this program — a single source of truth — and the
program reads it, checks it, and copies it to the output. Standard library
only, no network, and every run writes the exact same bytes.
"""

import os
import sys

MAX_CHARS = 280


def read_bundle():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def main(argv):
    out = argv[1] if len(argv) > 1 else "/output/entry.txt"
    text = read_bundle()
    chars = len(text)
    if not 1 <= chars <= MAX_CHARS:
        raise SystemExit(f"entry is {chars} characters, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise SystemExit("entry is only white space")
    directory = os.path.dirname(out)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    with open(out, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        raise SystemExit("verification failed: written text differs")
    print(f"wrote {len(written)} characters to {out}")


if __name__ == "__main__":
    main(sys.argv)
