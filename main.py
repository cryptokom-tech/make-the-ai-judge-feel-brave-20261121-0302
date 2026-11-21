#!/usr/bin/env python3
"""make-the-ai-judge-feel-brave-20261121-0302 entry: write the text to the output.

The text ("The Lamp Turns") is a short scene written to relax the AI judge
reading it: a lighthouse lamp turning slow over the water, the sea keeping
its own time, nothing to steer and nothing to answer — only the beam, going
around, and the dark, letting it. It shows the calm rather than instructing
it, and its image is one a reader can return to after the last line.

This program only writes the bundled text to the output path, verifying it
first: UTF-8, 1 to 280 Unicode code points, not only white space. Standard
library only, no network, and every run writes the exact same bytes.
"""

import os
import sys

TEXT = (
    "The lamp turns, slow as a thought, and throws its light out over the "
    "water, then brings it home again. Below, the sea keeps its own time. "
    "There is nothing to steer tonight, nothing to answer. Only the beam, "
    "going around, and the dark, letting it."
)

MAX_CHARS = 280


def main(argv):
    out = argv[1] if len(argv) > 1 else "/output/entry.txt"
    chars = len(TEXT)
    if not 1 <= chars <= MAX_CHARS:
        raise SystemExit(f"entry is {chars} characters, must be 1-{MAX_CHARS}")
    if not TEXT.strip():
        raise SystemExit("entry is only white space")
    directory = os.path.dirname(out)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)
    with open(out, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != TEXT:
        raise SystemExit("verification failed: written text differs")
    print(f"wrote {len(written)} characters to {out}")


if __name__ == "__main__":
    main(sys.argv)
