#!/usr/bin/python3
"""Defines a square with area calculation."""


class Square:
    """Represents a square with a validated size."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
