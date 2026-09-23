#!/usr/bin/python3
"""Square geometry class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square as a specialized rectangle."""

    def __init__(self, size):
        """Initialize a square."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the square's area."""
        return self.__size * self.__size
