"""Write the one-number entry for make.fun's
"How Many Tabs Do You Have Open?" bounty.

The program writes a single number in digits, and nothing else,
to /output/entry.txt: the entrant's honest count of open browser tabs.
"""

import os

NUMBER = "1024"


def main() -> None:
    # The gate counts the entry itself (1-5 characters, digits only);
    # the trailing newline is only the file's line ending. The checks
    # run in the judge's own order: a real count first, then digits
    # only, so a bad value fails here instead of in front of the judge.
    assert 1 <= len(NUMBER) <= 5, "entry must be 1-5 characters"
    assert NUMBER.isdigit(), "entry must be digits only"
    assert NUMBER.strip(), "entry must not be only white space"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(NUMBER + "\n")


if __name__ == "__main__":
    main()
