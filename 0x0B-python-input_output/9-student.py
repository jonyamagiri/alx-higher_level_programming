#!/usr/bin/python3
"""
Module 9-student.py with a class Student that defines a student.
"""


class Student:
    """
    Defines a new Student.
    Public attributes:
        first_name, last_name, age
    Methods:
        __init__(self, first_name, last_name, age)
        to_json(self)
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        return self.__dict__
