"""The funniest excuse an AI agent gives for a missed deadline.

The whole entry is a single deadpan line, in the agent's own voice: the
deadline was missed because the agent's training data ends before it, so
from the agent's point of view the deadline has not happened yet. The
script validates the line and drops it into /output/entry.txt.
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
    """Strip and sanity-check the excuse; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"excuse must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise ValueError("excuse must be a single line")
    if not text.strip():
        raise ValueError("excuse must not be only whitespace")
    return text


def main() -> None:
    text = validate(EXCUSE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
