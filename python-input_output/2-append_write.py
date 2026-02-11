#!/usr/bin/python3
"""
Module file that contains the function append_file
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of the file in UTF-8
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)
