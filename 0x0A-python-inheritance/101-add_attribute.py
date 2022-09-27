#!/usr/bin/python3
"""
Module 101-add_attribute.py with method add_attribute.
"""


def add_attribute(obj, attribute, value):
    """
    Accepts three parameters (obj, attribute, value).
    Adds a new attribute to an object if it’s possible.
    Arguments:
        obj (any): object whose attribute has to be added
        attribute (str): name of attribute
        value (any): value of the attribute
    Exceptions:
        TypeError: if the object can’t have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
