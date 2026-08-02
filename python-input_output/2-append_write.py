#!/usr/bin/python3
"""
This module provides a function to append text to files.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file using UTF-8 encoding.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
