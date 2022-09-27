#!/usr/bin/python3
"""
Module 4-from_json_string.py with method to_json_string.
"""
import json


def from_json_string(my_str):
    """
    Accepts object (my_str).
    Returns an object (Python data structure) represented by a JSON string
    """
    decode_json = json.loads(my_str)
    return decode_json
