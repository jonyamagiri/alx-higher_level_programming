#!/usr/bin/python3
"""
Module base.py that defines a class Base (model for other classes in project).
With private class attribute __nb_objects.
"""


class Base:
    """Defines the class Base (model for other classes in project).
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
