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
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ".?:"
    for elem in punctuation:
        text = text.replace(elem, elem + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    new_lines = "\n".join(list_lines)
    print(new_lines, end="")
