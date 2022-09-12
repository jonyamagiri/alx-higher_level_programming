#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_integers = 0
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]), end="")
            print_integers += 1
        except (TypeError, ValueError):
            continue
    print()
    return print_integers
