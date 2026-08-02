#!/usr/bin/python3
"""
This module provides a function to read and print text files.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to standard output.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
