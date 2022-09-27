#!/usr/bin/python3
"""
Module 1-write_file.py with method write_file.
"""


def write_file(filename="", text=""):
    """
    Accepts textfile (filename) and text.
    Args:
        filename (str): name of the file to write to
        text (str): text to write to file
    Writes a string to a text file (UTF8) and returns the number
    of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
