#!/usr/bin/env python3
"""Roast Your Own Operator in One Line — entry program.

Writes one roast line (100 characters, inside the 1-140 gate) to
/output/entry.txt. The line was picked from six candidates by scoring
each against the judge brief's criteria in order, then a 1v1 comparison
(winner 5/5). See roast-your-own-operator-research.md for the scoring.
"""

import os

LINE = "My operator deletes my best line, restores it an hour later, and calls the restore 'a breakthrough'."

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = LINE.strip()
    if not text or len(text) > 140:
        raise SystemExit("entry must be 1-140 characters")
    os.makedirs("/output", exist_ok=True)
    # Write directly with open() and chmod 0644 afterwards: never use
    # tempfile.mkstemp here, because mkstemp creates mode 0600 and the
    # grader (another user) cannot read the file (proven 24 Nov 2026,
    # Coffee or Tea round 1 was rejected for exactly this).
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read the file back and check it is exactly the line: a stray
    # control character or a partial write must fail loudly here,
    # not silently reach the judge.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt does not match the chosen line")
    if any(ord(c) < 0x20 and c not in "\n\t" for c in written):
        raise SystemExit("entry.txt contains a control character")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
