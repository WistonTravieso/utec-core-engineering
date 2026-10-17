#!/usr/bin/env python3

def islower(c):
    return ord('a') <= ord(c) <= ord('z')

islower('a')  # True
islower('A')  # False
islower('3')  # False