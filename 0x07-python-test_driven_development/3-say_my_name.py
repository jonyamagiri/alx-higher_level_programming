#!/usr/bin/python3
"""
Module 3-say_my_name.py, with method say_my_name(first_name, last_name="").
Prints My name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """
    Accepts parameters first_name and last_name which must be strings.
    Prints My name is <first name> <last name>.
    """
    if first_name == "" and last_name == "":
        return None

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
