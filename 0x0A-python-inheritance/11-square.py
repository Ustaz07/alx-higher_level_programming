#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle (9-rectangle.py)."""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
        - size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
