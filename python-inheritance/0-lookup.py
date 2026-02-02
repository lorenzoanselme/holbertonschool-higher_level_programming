#!/usr/bin/python3
"""
This module provides a function to list all available
attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        A list of attribute and method names.
    """
    return dir(obj)
