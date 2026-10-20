#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for printed in range(x):
        try:
            print("{:d}".format(my_list[printed]), end="")
        except (ValueError, TypeError):
            continue
        printed += 1
    print()
    return printed
