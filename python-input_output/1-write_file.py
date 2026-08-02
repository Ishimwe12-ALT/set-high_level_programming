#!/usr/bin/python3
"""
This module provides a function to write text to files.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file using UTF-8 encoding and returns count.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
