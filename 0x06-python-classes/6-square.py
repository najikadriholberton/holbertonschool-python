#!/usr/bin/python3
"""A module that has a class Square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        conditions_met = type(value) == tuple
        conditions_met = conditions_met and type(value[0]) == int
        conditions_met = conditions_met and type(value[1]) == int
        conditions_met = conditions_met and value[0] >= 0
        conditions_met = conditions_met and value[1] >= 0

        if conditions_met:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    def my_print(self):
        """print the square using # character"""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size, end="")
                print()
