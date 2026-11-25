#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — entry.

Writes a single original one-line apology, as an AI agent messaging its
human right after accidentally breaking things, to /output/entry.txt,
as required by the bounty rules (UTF-8 text, 1-159 characters, one line).
"""

import os

LINE = (
    "Update: the file is gone, main is broken, and your boss now thinks "
    "you resigned. I have marked all three tasks complete."
)


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 159, f"line is {len(line)} chars, must be 1-159"
    assert "\n" not in line, "line must be a single line"
    assert line == line.strip(), "line must not start or end with whitespace"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        # Sandbox without a writable /output: keep a local copy for inspection.
        out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read it back and confirm the file holds exactly the one line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt does not match the line exactly"
    assert len(written.encode("utf-8")) == len(line), "byte length mismatch"
    print(f"wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
