#!/usr/bin/python3
"""
Module file that contains the function write_file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of characters
    written
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
