#!/usr/bin/python3
"""
Module 0-add_integer.py, with method add_integer(a, b=98).
Returns the addition of a and b.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers (a and b) that are integers or floats.
    a and b first casted to integers if they are float.
    Returns an integer: the addition of a and b.
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
