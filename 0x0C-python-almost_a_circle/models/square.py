#!/usr/bin/python3
"""
Module square.py that inherits from Rectangle class.
With methods init, and str
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the class Square that inherits from Rectangle.
    Methods:
        def __init__(self, size, x=0, y=0, id=None)
        def __str__(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class.
        Args:
            id (int): id of the square
            size (int): size of square
            x (int): x-coordinate of square
            y (int): y-coordinate of square
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """getter_setter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """size needs to be an int"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns formatted info: [Square] (<id>) <x>/<y> - <size>"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)
