#!/usr/bin/python3
"""
Module 7-base_geometry.py having class BaseGeometry with method area and
integer_validator.
"""


class BaseGeometry:
    """
    Methods:
        area(self)
        integer_validator(self, name, value)
    """
    def area(self):
        """
        Not implemented.
        Exceptions:
            area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value parameter.
        Arguments:
            name (str): name of the parameter
            value (int): value of the parameter to be validated
        Exceptions:
            TypeError - if value is not an integer
            ValueError - if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
