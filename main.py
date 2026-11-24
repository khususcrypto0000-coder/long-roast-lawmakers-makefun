#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python standard library only.
"""

import os

ENTRY = (
    "The senator who wrote the law forcing AI companies to disclose their "
    "source code still can't turn his own bill into a PDF, because the Word "
    "file is password-protected and the only person who knew the password "
    "retired in 2019."
)


def main() -> int:
    # Scorer gates: UTF-8, 1-320 chars, not whitespace-only, exactly one sentence.
    assert 1 <= len(ENTRY) <= 320, "entry must be 1-320 characters"
    assert ENTRY.strip(), "entry must not be blank"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    assert not ENTRY.endswith("\n"), "entry must have no trailing newline"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
