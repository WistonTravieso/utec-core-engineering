#!/usr/bin/env python3

for code in range(ord("a"), ord("z") + 1):
    if chr(code) in "qe":
        continue
    print(chr(code), end="")
