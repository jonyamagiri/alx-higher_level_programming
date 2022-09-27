#!/usr/bin/python3
"""
Module 11-square.py with class Square that inherits class Rectangle.
Has instantiation with private attribute size and method str.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines class Square that inherits class Rectangle.
    Methods:
        __init__(self, size)
        __str__(self)
    """

    def __init__(self, size):
        """
        Initializes the class Square.
        Arguments:
            size (int): length of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns square description as: [Square] <width>/<height>"""
        string = "[{}] {}/{}".format(self.__class__.__name__,
                                     self.__size, self.__size)
        return string
