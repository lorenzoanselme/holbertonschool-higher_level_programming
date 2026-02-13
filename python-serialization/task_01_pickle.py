#!/usr/bin/python3
"""
This module contains a class for creating custom objects and methods for
serializing and deserializing them using the pickle module.
"""
import pickle


class CustomObject:
    """
    A class representing a custom object with attributes and methods for
    serialization and deserialization.
    """
    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject with the given attributes.
        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the CustomObject.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the CustomObject and saves it to a file using pickle.
        Returns None if an error occurs.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a CustomObject from a file using pickle.
        Returns None if the file does not exist or is corrupted.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None
