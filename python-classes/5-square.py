#!/usr/bin/python3
"""This module defines a Square class with printing capabilities."""


class Square:
    """This class represents a square with a controlled size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square instance with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating its value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the current square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the character '#'."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
