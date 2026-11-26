"""Loading Screen Gold: write one loading-screen tip to entry.txt.

Deterministic, stdlib-only, no network. Writes the tip byte-identically
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
"""

import os

TIP = (
    "Tip: your agent is re-reading the same file for the fifth time, "
    "just like you. Neither of you is stuck \u2014 you are both stalling "
    "before the scary part. Breathe."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
