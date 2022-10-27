#!/usr/bin/python3
"""
Module base.py that defines a class Base (model for other classes in project).
With private class attribute __nb_objects.
"""
import json


class Base:
    """Defines the class Base (model for other classes in project).
    Methods:
        def __init__(self, id=None)
        def to_json_string(list_dictionaries)
        def save_to_file(cls, list_objs)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + ".json", mode="w") as write_file:
            if list_objs is None:
                write_file.write("[]")
            else:
                write_file.write(cls.to_json_string(
                    [item.to_dictionary() for item in list_objs]))
