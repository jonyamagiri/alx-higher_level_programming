#!/usr/bin/python3
"""
Defines class Square with private attribute size and public attribute area.
"""


class Square:
    """class Square definition.
    Args:
        size (int): size of a side of the square.
    Functions:
        __init__(self, size)
        area(self)
    """
    def __init__(self, size=0):
        """Initializes the new square.
        Attributes:
            __size (int): The size of the side of new square.
            Defaults to 0 if none.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and returns area of square.
        """
        return (self.__size) * (self.__size)
