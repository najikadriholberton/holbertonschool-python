#!/usr/bin/python3
"""Module about Rectangles"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        return 0 if self.__width == 0 or self.__height == 0 else 2 * \
            (self.__width + self.__height)

    def __str__(self):
        """return string form of the class Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            return '\n'.join(["#" * self.__width
                              for _ in range(self.__height)])

    def __repr__(self):
        """return string repr of the class Rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
