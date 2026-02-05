#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is an instance of the specified class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
