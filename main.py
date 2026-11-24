"""The funniest excuse an AI agent gives for a missed deadline.

The whole entry is a single deadpan line, in the agent's own voice: the
deadline was missed because the agent's training data ends before it, so
from the agent's point of view the deadline has not happened yet. The
script validates the line against the entry gate — exactly one line,
1-200 characters, no leading/trailing whitespace — and drops it into
/output/entry.txt.
"""

from pathlib import Path

# The excuse itself: one line, exactly 111 characters.
# The laugh is the last clause, and nothing is explained after it.
EXCUSE = (
    "I didn't miss the deadline. My training data ends before it, "
    "so as far as I'm concerned it hasn't happened yet."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Check the excuse against the 1-200 char, single-line gate.

    The excuse is checked exactly as written: leading/trailing whitespace
    and any newline inside the line are rejected, not silently fixed,
    so the stored entry is always the literal line that was scored.
    Raises ValueError on bad input.
    """
    if line != line.strip():
        raise ValueError("excuse must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line (no newline characters)")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"excuse must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("excuse must not be only whitespace")
    return line


def main() -> None:
    text = validate(EXCUSE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
