#!/usr/bin/python3
"""
Module 8-rectangle.py with class Rectangle that inherits class BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines class Rectangle that inherits class BaseGeometry.
    Methods:
        __init__(self, width, height)
    """
    def __init__(self, width, height):
        """
        Initializes the class Rectangle.
        Arguments:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
