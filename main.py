#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint — a make.fun one-line entry.

The program writes the entry text to /output/entry.txt, where the
competition's sealed scorer reads it.
"""

from pathlib import Path

ENTRY = "Our standup now has a slide deck, an agenda, and a follow-up meeting to discuss why the standup took so long."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    """Write the entry text to the output path."""
    text = ENTRY.strip()
    assert text, "entry text must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
