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
        def from_json_string(json_string)
        def save_to_file(cls, list_objs)
        def create(cls, **dictionary)
        def load_from_file(cls)
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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if type(json_string) != str or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        with open(cls.__name__ + ".json", mode="w") as write_file:
            if list_objs is None:
                write_file.write("[]")
            else:
                write_file.write(cls.to_json_string(
                    [item.to_dictionary() for item in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, mode="r") as read_file:
                list_dicts = Base.from_json_string(read_file.read())
                return [cls.create(**item) for item in list_dicts]
        except IOError:
            return []
