#!/usr/bin/python3
"""
Module file that contains the function to_json_string
"""
import json


def to_json_strings(my_obj):
    """
    Returns the JSON representation of an object
    """
    return json.dumps(my_obj)
