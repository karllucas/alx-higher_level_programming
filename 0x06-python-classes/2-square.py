#!/usr/bin/python3
# 2-square.py
"""Define a class Sqaure."""

class Sqaure:
    """Represent a sqaure."""
    def __init__(self, size=0):
        """Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
