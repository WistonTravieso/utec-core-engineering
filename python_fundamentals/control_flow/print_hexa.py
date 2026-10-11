#!/usr/bin/env python3

for value in range(0, 99):
    print("{value:d} = 0x{value:x}".format(value, hex(value)))
