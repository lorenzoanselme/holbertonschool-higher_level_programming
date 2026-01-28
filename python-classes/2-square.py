#!/usr/bin/python3
"""This module defines a Square class with size validation."""


class Square:
    """This class represents a square defined by a validated size."""

    def __init__(self, size=0):
        """Initialize a new Square instance with a validated size value."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
