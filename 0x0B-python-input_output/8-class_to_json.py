#!/usr/bin/python3
"""
Module 8-class_to_json.py with method class_to_json.
"""


def class_to_json(obj):
    """
    Accepts parameter obj (an instance of a class).
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.
    """
    return obj.__dict__
