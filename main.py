#!/usr/bin/env python3
"""One Line to Your Younger Self entry.

Writes exactly one line to /output/entry.txt (1-200 UTF-8 chars, not
only whitespace), as the sealed scorer's gate requires. Deterministic,
stdlib only, no network, no secrets, no randomness.
"""

import os

ENTRY = "Your mum was right about the sunscreen and wrong about the haircut \u2014 forgive her for the second one first."


def main():
    # Gate self-check: the sealed scorer requires /output/entry.txt to be
    # UTF-8 text of 1 to 200 characters, not only whitespace. Fail loudly
    # here instead of shipping a rejected entry.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY == ENTRY.strip(), "entry has leading/trailing whitespace"
    assert all(ord(c) >= 32 for c in ENTRY), "entry has control characters"
    # Judge criterion 1: the line must be told to a younger self, in the
    # second person, not a slogan addressed to nobody in particular.
    assert "your" in ENTRY.lower(), "entry must address the younger self"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back byte-for-byte: what is on disk must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"


if __name__ == "__main__":
    main()
