#!/usr/bin/env python3
"""The Worst Pizza Topping — one funny line, plain Python stdlib.

The entry is a single line: the grader reads /output/entry.txt, so the
output must be exactly one line plus a trailing newline, nothing more.
"""

import os

ENTRY = "Pineapple: a fruit salad that lost a bet and landed on my pizza \u2014 sweet, soggy, and legally not a topping."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)

if __name__ == "__main__":
    main()
