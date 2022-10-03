#!/usr/bin/python3
"""
Module rectangle.py that inherits from Base.
With private instance attributes width, height, x and y and super class id.
"""
from models.base import Base


class Rectangle(Base):
    """Defines the class Rectangle that inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the class.
        Args:
            id (int): id of the rectangle
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x-coordinate of rectangle
            y (int): y-coordinate of rectangle
        Exceptions:
            TypeError - If the input (width, height, x, y) is not an integer
            ValueError - If width or height is under or equals 0
            ValueError - If x or y is under 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter_setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter_setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter_setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter_setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
