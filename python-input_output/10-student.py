#!/usr/bin/python3
"""
Module that defines a Student class with attributes first_name, last_name, and
age,
and a method to_json that returns the dictionary representation of the Student
instance.
"""


class Student:
    """
    Defines a Student class with attributes first_name, last_name, and age,
    and a method to_json that returns the dictionary representation of the
    Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first_name, last_name,
        and age.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the Student instance.
        Args:
            attrs (list): Optional list of attribute names to retrieve.
                         If None, all attributes are retrieved.
        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if
                    hasattr(self, attr)}
