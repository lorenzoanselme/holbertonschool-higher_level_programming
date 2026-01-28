#!/usr/bin/python3
"""This module defines a Square class that supports size comparison."""


class Square:
    """This class represents a square that can be compared by its area."""

    def __init__(self, size=0):
        """Initialize a new Square instance with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validating its value."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the current square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares for equality based on their area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare two squares for inequality based on their area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is smaller than another square by area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is smaller than or equal to another."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is larger than another square by area."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is larger than or equal to another."""
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
