#!/usr/bin/python3
"""
A class Rectangle with private attributes width and height,
public attribute number_of_instances and print_symbol.
"""


class Rectangle:
    """Defines the class Rectangle with private attributes width and height.
    Arguments:
        width (int)
        height (int)
    Attributes:
        number_of_instances (int): counts instances of the class
        print_symbol (any type): Used as symbol for string representation
    Methods:
        __init__(self, width=0, height=0)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the class."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Takes the arguments width and height.
        Returns the rectangle area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Takes the arguments width and height.
        Returns the rectangle perimeter 2*(width + height).
        If width or height is equal to 0, perimeter is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Takes the arguments width and height.
        Prints the rectangle with 'print_symbol' character.
        if width or height is equal to 0, return an empty string.
        """
        grid = ""
        if self.__width == 0 or self.__height == 0:
            return grid
        for i in range(self.__height):
            for j in range(self.__width):
                print(self.print_symbol, end="")
            if i != self.__height - 1:
                print()
        return grid

    def __repr__(self):
        """
        Takes the arguments width and height.
        Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print the message 'Bye rectangle...'
        when instance of the class Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
