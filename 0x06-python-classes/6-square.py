#!/usr/bin/python3
"""
Defines class Square with private attribute size & position, and
public attribute area.
Can access and update size and position.
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
        position(self)
        position(self, value)
        area(self)
        my_print(self)
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the new square.
        Attributes:
            __size (int): The size of the side of new square.
            Defaults to 0 if none. Don't use __size to call setter.
            position (int): tuple of two positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter. Retrieves position of the square."""
        return (self.__position)

    @size.setter
    def position(self, value):
        """Setter.
        Args:
            value: sets position to tuple if value is tuple of 2 positive ints
        """
        if type(value) is not tuple or len(value) != 2 or \
                type(value[0]) is not int or type(value[1]) is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns area of square.
        """
        return (self.__size) * (self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
