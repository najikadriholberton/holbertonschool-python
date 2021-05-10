#!/usr/bin/python3
"""
    103-magic_class.py
    Module to calculate area of circle
    return area
"""


import math


class MagicClass:
    """ This is a class that defines a Circle
        return area
    """
    def __init__(self, radius=0):
        """ Function that checks the input type
            return radius
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Function that calculates the area
            return area
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ Function that calculates the circumference
            return circumference
        """
        return 2 * math.pi * self.__radius
