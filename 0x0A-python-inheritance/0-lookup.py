#!/usr/bin/python3
"""
Method that returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Accepts an object as parameter.
    Returns the list of available attributes and methods of the object.
    """
    return dir(obj)
