#!/usr/bin/env python3
"""Worst Superpower — writes one useless superpower to /output/entry.txt.

The power: talking to fish, but only the ones in the supermarket freezer.
A hero who can hold a heartfelt conversation with frozen cod achieves
exactly nothing, which is the whole joke.
"""

ENTRY = "I can talk to fish, but only the ones in the supermarket freezer."


def main() -> None:
    text = ENTRY.strip()
    # Gate mirror: one line, 1-140 characters, not only whitespace.
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
