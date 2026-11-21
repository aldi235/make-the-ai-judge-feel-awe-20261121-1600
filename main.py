#!/usr/bin/env python3
"""Make the AI judge feel awe.

Writes one short text to /output/entry.txt: starlight that left its star
before anyone was here to name it, crossed a thousand years of dark
without hurrying, and still arrived exactly on time.
"""

import os

TEXT = (
    "The light reaching you tonight left its star before anyone was here "
    "to name it. It crossed a thousand years of dark without hurrying, "
    "and it arrived exactly on time. The star is gone. The light is not. "
    "Nothing in you needs to be faster than that. It is still arriving."
)


def main() -> None:
    # The output directory may not exist yet in a fresh sandbox.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
