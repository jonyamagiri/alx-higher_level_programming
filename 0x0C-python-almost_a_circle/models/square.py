#!/usr/bin/python3
"""
Module square.py that inherits from Rectangle class.
With methods init, str, update and to_dictionary.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the class Square that inherits from Rectangle.
    Methods:
        def __init__(self, size, x=0, y=0, id=None)
        def __str__(self)
        def update(self, *args, **kwargs)
        def to_dictionary(self)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the class.
        Args:
            id (int): id of the square
            size (int): size of square
            x (int): x-coordinate of square
            y (int): y-coordinate of square
        """
        super().__init__(size, size, x=x, y=y, id=id)

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

    def update(self, *args, **kwargs):
        """Updates the class Square by assigning an argument
        to each attribute."""
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Receives kwargs and returns dictionary representation"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
