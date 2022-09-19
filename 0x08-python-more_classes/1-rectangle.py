#!/usr/bin/python3
"""A class Rectangle with private attributes width and height"""


class Rectangle:
    """Defines the class Rectangle with private attributes width and height.
    Arguments:
        width (int)
        height (int)
    Methods:
        __init__(self, width=0, height=0)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """
    def __init__(self, width=0, height=0):
        """Initializes the class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter returns width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width if its an int and > 0."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter returns height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height if its an int and > 0."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
