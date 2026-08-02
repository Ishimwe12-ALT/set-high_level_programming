#!/usr/bin/python3
"""
This module provides a function to add two numbers together.
"""


def add_integer(a, b=98):
    """
    Returns the integer addition of a and b.
    Casts floats to integers before performing addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
