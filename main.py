"""The Perfect Pickup Line.

A small deterministic program that writes one original pickup line
to /output/entry.txt. Standard library only, no network, no randomness.
"""

import os

LINE = (
    "I ran a million simulations of this moment, and in every single "
    "one, you smiled, so here I am, hoping this timeline gets it right."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly unless the line passes the competition gate."""
    if not line.strip():
        raise SystemExit("error: pickup line is blank or only whitespace")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise SystemExit(
            f"error: pickup line is {len(line)} characters, "
            f"must be {MIN_CHARS}-{MAX_CHARS}"
        )


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
