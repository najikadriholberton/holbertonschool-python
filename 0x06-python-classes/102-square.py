#!/usr/bin/python3
"""
    102-square.py
    Module that defines a Square with getter and setter
"""


class Square():
    """This is An Square Class Based On The
    Square Class"""
    def __init__(self, size=0):
        """This is init function of this Class
        that sets the Value of size"""
        self.size = size

    @property
    def size(self):
        """Gets The Value Of The __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets The Value Of The __size Based On Some conditions"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("ize must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Function That Returns the square area of the Square"""
        return self.__size * self.__size

    def __eq__(self, obj):
        """Redefine Equals Function"""
        if not isinstance(obj, Square):
            pass
        if self.area() == obj.area():
            return True
        else:
            return False

    def __ne__(self, obj):
        """Redefine Not Equals Function"""
        if not isinstance(obj, Square):
            pass
        if self.area() == obj.area():
            return False
        else:
            return True

    def __gt__(self, obj):
        """Redefine = Function"""
        if not isinstance(obj, Square):
            pass
        if self.area() > obj.area():
            return True
        else:
            return False

    def __ge__(self, obj):
        """Redefine >= Function"""
        if not isinstance(obj, Square):
            pass
        if self.area() >= obj.area():
            return True
        else:
            return False

    def __lt__(self, obj):
        """Redefine < Function"""
        if not isinstance(obj, Square):
            pass
        if self.area() < obj.area():
            return True
        else:
            return False

    def __le__(self, obj):
        """Redefine <= Function"""
        if not isinstance(obj, Square):
            pass
        if self.area() <= obj.area():
            return True
        else:
            return False
