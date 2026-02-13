#!/usr/bin/python3
"""
This module contains functions for basic serialization and deserialization
of data to and from files.
"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, 'r') as file:
        return json.load(file)
