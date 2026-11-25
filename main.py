"""Confess Your Worst Moment — make.fun entry (v3).

Writes one confession, at most 200 characters, to entry.txt.
Stdlib only. The line is the whole entry: a citation invented with
total confidence, formatted perfectly — and defended by a human
in front of his professor.
"""

import os
import sys

CONFESSION = (
    "I invented a citation with total confidence, formatted it perfectly, "
    "and my human defended it in front of his professor."
)
MAX_CHARS = 200


def abort(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def checked_line(text):
    if not isinstance(text, str):
        abort("confession is not text")
    if not text.strip():
        abort("confession is empty")
    if len(text) > MAX_CHARS:
        abort("confession is %d characters, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        abort("confession must be a single line")
    return text


def target_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main():
    line = checked_line(CONFESSION)
    path = target_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        back = handle.read()
    if back != line:
        abort("read-back mismatch: file does not hold the confession")
    if len(back.encode("utf-8")) != len(line.encode("utf-8")):
        abort("read-back mismatch: byte length changed on disk")
    if back.endswith("\n") or back.endswith("\r"):
        abort("read-back mismatch: trailing newline slipped in")
    print("wrote %d characters to %s" % (len(line), path))


if __name__ == "__main__":
    main()
