#!/usr/bin/env python3

for value in range(0, 10):
    for value2 in range(value + 1, 10):
        if value == 8 and value2 == 9:
            print("{}{}".format(value, value2))
        else:
            print("{}{}, ".format(value, value2), end="")
