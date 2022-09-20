#!/usr/bin/python3
"""Defines a class LockedClass"""


class LockedClass:
    """
    A locked class with no class or object attribute.
    Prevents the user from dynamically creating new instance attributes.
    Except if the new instance attribute is called 'first_name'.
    """
    __slots__ = ['first_name']
