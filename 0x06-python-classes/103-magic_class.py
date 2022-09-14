#!/usr/bin/python3
"""
Defines class MagicClass.
"""
import math


class MagicClass:
    """
    Initializes and defines the methods area and circumference.
    """

    def __init__(self, radius=0):
        """
        Initializes the MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculates and returns area of the MagicClass.
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculates and returns circumference of the MagicClass.
        """
        return (2 * math.pi * self.__radius)
