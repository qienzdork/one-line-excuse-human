"""One-line excuse an AI agent gives its human for missing a deadline.

Writes the excuse to /output/entry.txt by default, or to the path in
the $OUTPUT_PATH environment variable when set. Deterministic, stdlib
only, no network, no randomness.
"""

import os

EXCUSE = "I didn't miss the deadline \u2014 I hallucinated a later one and believed it."


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
