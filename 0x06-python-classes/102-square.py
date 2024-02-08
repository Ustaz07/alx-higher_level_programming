#!/usr/bin/python3
"""Define a class Square that defines a square based on 4-square.py."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new instance of Square.

        Args:
            size (float or int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (float or int): The size to set.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """Check if the area of the square is less than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than the other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the square is less than or equal to the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less than or equal to the other, False otherwise.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """Check if the area of the square is equal to the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is equal to the other, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if the area of the square is not equal to the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is not equal to the other, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if the area of the square is greater than the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than the other, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the square is greater than or equal to the other.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater than or equal to the other, False otherwise.
        """
        return self.area() >= other.area()
