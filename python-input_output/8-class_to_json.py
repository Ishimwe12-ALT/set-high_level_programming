#!/usr/bin/python3
"""
This module contains a function returning dictionary descriptions of objects.
"""


def class_to_json(obj):
    """
    Returns the dictionary representation for JSON serialization of an object.
    """
    return obj.__dict__
