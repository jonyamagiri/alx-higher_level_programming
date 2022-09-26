#!/usr/bin/python3
"""
Module 4-inherits_from.py with method inherits_from(obj, a_class).
Checks if object is an inherited instance (directly or indirectly) of class.
"""


def inherits_from(obj, a_class):
    """
    Accepts two parameters (obj and a_class).
    Checks if object is an inherited instance of class
    (inherited directly or indirectly).
    Return:
        True - if the object is an inherited instance of the specified class
                (directly or indirectly)
        False - otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
