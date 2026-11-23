"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set for local testing).
No network calls, no dependencies — standard library only.
"""

import os

ENTRY = (
    "I gave my Wi-Fi password to one guest, and now my router has "
    "a bigger social life than I do."
)


def main() -> None:
    # Guard: the gate requires 1-200 UTF-8 characters, a single line.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the gate counts 1-200 characters, so the file
    # holds exactly the line, nothing more.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
