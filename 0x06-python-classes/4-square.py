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
        size(self)
        size(self, value)
        area(self)
    """
    def __init__(self, size=0):
        """Initializes the new square.
        Attributes:
            __size (int): The size of the side of new square.
            Defaults to 0 if none.
        """
        self.size = size

    @property
    def size(self):
        """Getter. Retrieves size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter.
        Args:
            value: sets size to value, if int and >= 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns area of square.
        """
        return (self.__size) * (self.__size)
