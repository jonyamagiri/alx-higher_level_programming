#!/usr/bin/python3
"""
Defines class Square with private attribute size and public attribute area.
Can access and update size.
Prints in stdout the square with the character #
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
        print(self)
    """
    def __init__(self, size=0):
        """Initializes the new square.
        Attributes:
            __size (int): The size of the side of new square.
            Defaults to 0 if none.
            Don't use __size to call setter.
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

    def my_print(self):
        """Prints in stdout the square with the character #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
