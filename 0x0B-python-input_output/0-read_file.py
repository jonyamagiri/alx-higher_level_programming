#!/usr/bin/python3
"""
Module 0-read_file.py with method read_file.
"""


def read_file(filename=""):
    """
    Accepts textfile (filename).
    Reads the text file (UTF8) and prints it to stdout.
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
