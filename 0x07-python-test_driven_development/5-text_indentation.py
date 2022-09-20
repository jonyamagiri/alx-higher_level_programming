#!/usr/bin/python3
"""
Module 5-text_indentation.py, with method text_indentation(text).
prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Accepts parameter text (a str).
    Prints text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    punctuation = [".", "?", ":"]
