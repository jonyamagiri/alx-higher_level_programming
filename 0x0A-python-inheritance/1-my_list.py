#!/usr/bin/python3
"""
Module 1-my_list.py that inherits (list) with method def print_sorted(self).
Prints the list, but sorted (ascending sort).
"""


class MyList(list):
    """
    Defines class MyList that inherits list.
    Methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """Prints elements of list (ints) sorted in ascending order"""
        print(sorted(self))
