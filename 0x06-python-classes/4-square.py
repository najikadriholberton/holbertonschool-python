#!/usr/bin/python3
"""A module that has a class Square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        self.__size = val

        size = self.__size

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
