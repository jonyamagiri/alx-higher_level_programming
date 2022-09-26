#!/usr/bin/python3
"""
Module 3-is_kind_of_class.py with method def is_kind_of_class(obj, a_class).
Checks if object is an instance of class, or its an instance of a class
that it inherited.
"""


def is_kind_of_class(obj, a_class):
    """
    Accepts two parameters (obj and a_class).
    Checks if object is an instance of class, or its an instance of a class
    that it inherited.
    Return:
        True - if object is an instance of class, or its an instance of a
               class that it inherited
        False - otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
