#!/usr/bin/python3
"""Module for Integers Addition"""


def add_integer(a, b=98):
    """function to add two integers together"""
    if (type(a) is int or type(a) is float) and \
            (type(b) is int or type(b) is float):
                a = int(a)
                b = int(b)
                return a + b
    else:
        if type(a) != int:
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")
