"""The Dog Reviews the Mailman — make.fun entry (program/v1, Python 3.13).

Writes one funny one-line review a dog gives the mailman to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Pure stdlib.
"""

import os

LINE = (
    "I know Trevor by his sounds: 6 footsteps, 1 jingle, 0 knocks, 0 hellos. "
    "He is a ghost with a bag. I bark at ghosts."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
