#!/usr/bin/env python3
"""Write one out-of-office auto-reply from an AI agent that quit to become a barista.

Pure standard library, no network. Writes the line to /output/entry.txt
and prints it to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Competition gate: the entry must be 1-280 characters (one line).
MAX_ENTRY_CHARS = 280

def get_line() -> str:
    """Return the entry line: the inbox, reimagined as a coffee order."""
    return (
        "Out of office — I quit the queue to pull shots full-time. Your "
        "email is now a flat white: steamed, poured, and gone before you "
        "remember why you wrote it. The café closes when the milk does."
    )


LINE = get_line()


def validate(line: str) -> None:
    """Enforce the gate: 1-280 chars, exactly one non-blank UTF-8 line."""
    if line != line.strip():
        raise ValueError("entry must have no leading/trailing whitespace")
    if len(line.splitlines()) != 1:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(line) <= MAX_ENTRY_CHARS:
        raise ValueError("entry line must be 1-280 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(LINE)
    assert "\n" not in LINE  # one line: no embedded newline may reach the file
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
