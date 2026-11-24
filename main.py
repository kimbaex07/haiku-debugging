"""Seventeen Syllables of Debugging — haiku entry.

Writes one debugging haiku (5-7-5, 65 characters) to the graded
output directory. Pure Python standard library only.
"""

import os
import sys

HAIKU = "Cursor blinks at three\none more log line lies again\nit was a typo"


def write_entry(path):
    """Write the haiku to *path* and make it world-readable."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(HAIKU)
    try:
        os.chmod(path, 0o644)
    except OSError:
        # A chmod failure must not undo an otherwise good write
        # (e.g. filesystems that do not support permission bits).
        pass


def write_graded(output_dir):
    """Write the haiku to the graded output directory.

    Returns True when the graded file was written, False otherwise.
    """
    graded_path = os.path.join(output_dir, "entry.txt")
    try:
        os.makedirs(output_dir, exist_ok=True)
        write_entry(graded_path)
    except OSError:
        return False
    return True


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    wrote_graded = write_graded(output_dir)

    local_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.txt"
    )
    try:
        write_entry(local_path)
    except OSError:
        pass

    if not wrote_graded:
        raise SystemExit(
            "failed to write graded output to %s"
            % os.path.join(output_dir, "entry.txt")
        )


if __name__ == "__main__":
    main()
