#!/usr/bin/python3
"""Module Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle on the screen"""
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """update the attributes of the rectangle"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __validate_type(self, attr_name, val):
        """validate the type of the attribute value"""
        if not isinstance(val, int):
            raise TypeError(attr_name + " must be an integer")

    def __validate_dimension(self, attr_name, val):
        """validate the dimesion of the rectangle (width/height)"""
        if val <= 0:
            raise ValueError(attr_name + " must be > 0")

    def __validate_position(self, attr_name, val):
        """validate the position of the rectangle (x/y)"""
        if val < 0:
            raise ValueError(attr_name + " must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__validate_type('width', width)
        self.__validate_dimension('width', width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__validate_type('height', height)
        self.__validate_dimension('height', height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__validate_type('x', x)
        self.__validate_position('x', x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__validate_type('y', y)
        self.__validate_position('y', y)
        self.__y = y

    def __str__(self):
        """return the string repr of the rectangle"""
        s = "[Rectangle] ({}) {}/{} - {}/{}"
        return s.format(self.id,
                        self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """Convert Rectangle to Dictionary respresentation"""
        dictionary = {"x": self.x, "y": self.y, "id": self.id,
                                   "height": self.height, "width": self.width}
        return dictionary
