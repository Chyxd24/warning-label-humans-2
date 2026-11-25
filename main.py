"""Warning Label for Humans: One-Line Big Laugh.

Writes one safety warning label for humans (<=160 chars) to /output/entry.txt.
Joke first, plausible second; the laugh lands on the last words.
"""
import os

OUT_DIR = "/output"
LABEL = ("WARNING: human may attempt to fix sleep schedule at 2 a.m. "
         "by reading about sleep. Known side effect: becoming an expert "
         "on sleep while getting none.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(LABEL) <= 160, len(LABEL)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LABEL)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == LABEL
    print(f"wrote {len(LABEL)} chars")


if __name__ == "__main__":
    main()
