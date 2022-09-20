#!/usr/bin/python3
"""
Module 4-print_square.py, with method print_square(size).
Prints a square with the character #.
"""


def print_square(size):
    """
    Accepts parameter size (an int) which is the length of the square.
    Size must be an integer and >= 0
    Prints a square with the character #.
    """
    print_symbol = "#"

    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return None

    for i in range(size):
        for j in range(size):
            print(print_symbol, end="")
        print()
