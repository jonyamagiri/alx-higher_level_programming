#!/usr/bin/python3
"""
Module 9-rectangle.py with class Rectangle that inherits class BaseGeometry.
Has methods area and str
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defines class Rectangle that inherits class BaseGeometry.
    Methods:
        __init__(self, width, height)
        area(self)
        __str__(self)
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

    def area(self):
        """Implements parent class's area method."""
        return self.__width * self.__height

    def __str__(self):
        """Returns rectangle description as: [Rectangle] <width>/<height>"""
        string = "[{}] {}/{}".format(self.__class__.__name__,
                                     self.__width, self.__height)
        return string
