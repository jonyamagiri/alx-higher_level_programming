#!/usr/bin/python3
"""
Module 3-to_json_string.py with method to_json_string.
"""
import json


def to_json_string(my_obj):
    """
    Accepts object (my_obj).
    Returns the JSON representation of an object (string)
    """
    make_json = json.dumps(my_obj)
    return make_json
