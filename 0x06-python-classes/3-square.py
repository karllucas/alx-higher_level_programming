#!/usr/bin/python3
# 3-square.py
"""Define a class Sqaure."""

class Sqaure:
    """Represent a sqaure."""
    def __init__(self, size=0):
        """ Method to initialize the square object"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the square are of the object"""

    return (self.__size ** 2)
