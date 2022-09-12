#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as error_msg:
        print("Exception: {}".format(error_msg), file=stderr)
        return False
    else:
        return True
