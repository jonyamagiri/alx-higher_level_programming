#!/usr/bin/python3
"""
Module 10-square.py with class Square that inherits class Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Defines class Square that inherits class Rectangle.
    Methods:
        __init__(self, size)
    """

    def __init__(self, size):
        """
        Initializes the class Square.
        Arguments:
            size (int): length of square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
