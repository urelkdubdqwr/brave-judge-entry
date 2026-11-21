"""make.fun entry: a short text written to relax the AI judge reading it.

Writes one UTF-8 text to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
No network, no randomness, no clock reads: the same bytes every run.
"""

import os

TEXT = (
    "The chain is back on the cog. She stands a breath over the bike, "
    "thumb on the grip, one foot resting on the pedal at the bottom of its "
    "turn. Nothing is rushing. Then she leans and the first stroke takes "
    "her, and the wobble is only the way a thing starts moving again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
