#!/usr/bin/python3
"""
Module 2-is_same_class.py with method def is_same_class(obj, a_class).
Checks if obj is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Accepts two parameters (obj and a_class).
    Checks if obj is exactly an instance of the specified class.
    Return:
        True - if the object is exactly an instance of the specified class;
        False - otherwise
    """
    if type(obj) == a_class:
        return True
    return False
