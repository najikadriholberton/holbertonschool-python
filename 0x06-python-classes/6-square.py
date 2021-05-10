#!/usr/bin/python3
"""A module that has a class Square"""


class Square():
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """trying to add docstring here too"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get space position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set space position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(v) != int for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(v < 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print the square using # character"""
        if self.__size != 0:
            for k in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], "#" * self.__size)
        else:
            print()
