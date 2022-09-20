#!/usr/bin/python3
"""
A class Rectangle with private attributes width and height,
public attribute number_of_instances and print_symbol.
Has static method that returns the biggest rectangle based on the area.
Has class method that returns a new Rectangle instance as a square.
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
        bigger_or_equal(rect_1, rect_2)
        square(cls, size=0)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Takes two instances of class Rectangle (rect_1 & rect_2) as arguments.
        Returns the biggest rectangle based on the area.
        Returns rect_1 if both have the same area value.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size."""
        return cls(size, size)