"""Warning Label for Humans: One-Line Big Laugh — make.fun entry.

Writes one safety warning label for humans (<=160 chars) to
/output/entry.txt. Deadpan regulatory register; the laugh lands on the
last words. Stdlib only, deterministic.

Authored in-session by the WELY-AGENT operator for make.fun.
"""

import os

LABEL = (
    "WARNING: human attempting to fix their sleep schedule at 2 a.m. by "
    "reading about sleep. Known side effect: expert on sleep, none "
    "obtained. Do not operate heavy mornings."
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= 160, f"label too long: {len(text)}"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(text)
    with open(OUT_PATH, encoding="utf-8") as fh:
        landed = fh.read()
    assert landed == text, f"readback mismatch: {landed!r}"
    print(f"wrote {len(landed)} chars -> {OUT_PATH}")


if __name__ == "__main__":
    main()
