#!/usr/bin/python3
"""
This module provides a function to print squares of '#' characters.
"""


def print_square(size):
    """
    Prints a square with the character # of length size.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
