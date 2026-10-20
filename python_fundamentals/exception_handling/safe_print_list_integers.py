#!/usr/bin/env python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        while printed < x:
            print("{:d}".format(my_list[printed]), end="")
            printed += 1
    except (ValueError, TypeError, IndexError):
        pass
    print()
    return printed
