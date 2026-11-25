#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint (make.fun).

Writes the entry -- one short joke about office life, written to /output/entry.txt by a small Python program. -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

TEXT = 'The meeting that should have been an email has now spawned three follow-up meetings, each of which should also have been an email.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
