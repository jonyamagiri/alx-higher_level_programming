#!/usr/bin/python3
"""
Module 100-append_after.py with method append_after.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string.
    Args:
        filename (str): name of the file
        search_string (str): string being searched for within file
        new_string (str): string to insert
    """
    text = ""

    with open(filename, mode="r+", encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, mode="w") as wr:
        wr.write(text)
