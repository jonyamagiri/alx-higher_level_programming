#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (ZeroDivisionError, IndexError, TypeError, ValueError) as error_msg:
        print("Exception: {}".format(error_msg), file=stderr)
        return None
