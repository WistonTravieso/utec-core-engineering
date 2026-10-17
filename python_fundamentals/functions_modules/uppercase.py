#!/usr/bin/env python3

def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')


print(uppercase('Hello World!'))  # HELLO WORLD!
