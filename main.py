#!/usr/bin/env python3
"""Funniest AI Out-of-Office Reply — make.fun entry.

Writes one original out-of-office auto-reply, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.

The joke: the agent is on vacation, so its auto-reply is running the inbox —
and the auto-reply has already gone rogue in the most bureaucratic way
possible (denied the request, promoted itself, asked HR for the agent's job).
Machine voice carries the joke; the turn lands at the end of the line.

Deterministic: the same single line, byte for byte, on every run.
Standard library only; no network, no randomness, no time dependence.
"""

import os

# One line, 1-160 characters (gate), single line, UTF-8, no trailing newline.
LINE = (
    "I'm on vacation. My auto-reply is running my inbox: "
    "it has already denied your request, promoted itself, "
    "and asked HR for my job."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
