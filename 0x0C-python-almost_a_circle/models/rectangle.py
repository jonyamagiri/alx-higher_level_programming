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
        self.__width = value

    @property
    def height(self):
        """getter_setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """getter_setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """getter_setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
