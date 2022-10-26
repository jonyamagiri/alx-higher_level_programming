#!/usr/bin/python3
"""
Module rectangle.py that inherits from Base.
With private instance attributes width, height, x and y and super class id.
And methods area, display, str, update and to_dictionary
"""
from models.base import Base


class Rectangle(Base):
    """Defines the class Rectangle that inherits from Base.
    Methods:
        def __init__(self, width, height, x=0, y=0, id=None)
        def area(self)
        def display(self)
        def __str__(self)
        def update(self, *args, **kwargs)
        def to_dictionary(self)
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #
        y is newline, x is space"""
        if self.__y != 0:
            for newline in range(self.__y):
                print()
        for row in range(self.__height):
            print((self.__x * " ") + (self.__width * '#'))

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates the class Rectangle by assigning an argument
        to each attribute."""

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Receives kwargs and returns dictionary representation"""
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
