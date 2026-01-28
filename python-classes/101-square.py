#!/usr/bin/python3
"""This module defines a Square class with size and position handling."""


class Square:
    """This class represents a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance with size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validating its value."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integer"
            )
        self.__position = value

    def area(self):
        """Return the area of the current square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the same behavior as __str__."""
        print(self.__str__())

    def __str__(self):
        """Return a string representation of the square."""
        if self.__size == 0:
            return ""

        result = ""

        for _ in range(self.__position[1]):
            result += "\n"

        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if i != self.__size - 1:
                result += "\n"

        return result
