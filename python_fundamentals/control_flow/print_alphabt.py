#!/usr/bin/env python3

a = ""
for code in range(ord("a"), ord("z") + 1):
    char = chr(code)
    if char != "e" and char != "q":
        a += char

print(a)
