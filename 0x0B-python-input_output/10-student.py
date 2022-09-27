#!/usr/bin/python3
"""
Module 10-student.py with a class Student that defines a student.
Has method to_json that retrieves a dictionary representation of a
Student instance.
"""


class Student:
    """
    Defines a new Student.
    Public attributes:
        first_name, last_name, age
    Methods:
        __init__(self, first_name, last_name, age)
        to_json(self, attrs=None)
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Return:
            If attrs is a list of strings, only attribute names contained
            in this list must be retrieved.
            Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}
            for item in attrs:
                if item in self.__dict__.keys():
                    my_dict[item] = self.__dict__[item]
            return my_dict
