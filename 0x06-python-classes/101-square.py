#!/usr/bin/python3
"""
    6-square.py
    Module that defines a Square
    return area
"""


class Square:
    """ This is a class that defines a Square
        return area
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Function that checks the input type
            return size and position
        """
        self.__size = size
        self.__position = position
        if type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(v) != int for v in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(v < 0 for v in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Function that calculates the area
            return area
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Function that gets the size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Function that sets the size value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(value, int):
            self.__size = value

    @property
    def position(self):
        """ Function that gets the position value
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Function that sets the position value
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(v) != int for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(v < 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Function that prints the area based on the size and position
        """
        if self.__size != 0:
            for k in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for l in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def __repr__(self):
        """represent square"""
        result = ""
        if self.__size != 0:
            for k in range(self.__position[1]):
                result += "\n"

            for i in range(self.__size):
                for l in range(self.__position[0]):
                    result += " "
                for j in range(self.__size):
                    result += "#"
                result += "\n" if i < self.__size-1 else ""
        else:
            result += "\n"
        return result
