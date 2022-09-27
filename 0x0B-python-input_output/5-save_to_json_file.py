#!/usr/bin/python3
"""
Module 5-save_to_json_file.py with method save_to_json_file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Accepts parameters my_obj and filename
    Writes an Object to a text file, using a JSON representation.
    """
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
