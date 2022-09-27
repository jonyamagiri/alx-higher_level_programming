#!/usr/bin/python3
"""
Module 2-append_write.py with method append_write.
"""


def append_write(filename="", text=""):
    """
    Accepts textfile (filename) and text.
    Args:
        filename (str): name of the file to write to
        text (str): text to append to file
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
