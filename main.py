"""The Best Advice I Ever Got — one-line entry.

Writes the single sentence to /output/entry.txt (and prints it).
The line is one sentence, 200 characters at most, about the best
advice the writer ever received.
"""

from pathlib import Path

ENTRY = (
    "My grandfather told me never to make a promise when I was happy "
    "or a decision when I was angry, and thirty years on it is still "
    "the only rule I have never broken."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 200, f"entry is {len(text)} characters, over 200"
    assert text.count(".") == 1, "entry must be a single sentence"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    # Read it back to prove the written file matches the entry.
    assert out.read_text(encoding="utf-8").strip() == text
    print(text)


if __name__ == "__main__":
    main()
