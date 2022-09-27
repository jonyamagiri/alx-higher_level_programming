#!/usr/bin/python3
"""
Module 6-load_from_json_file.py with method load_from_json_file.
"""
import json


def load_from_json_file(filename):
    """
    Accepts parameter filename
    Creates an Object from a “JSON file”
    """
    with open(filename, mode="r") as f:
        return json.load(f)
