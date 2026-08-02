#!/usr/bin/python3
"""
This module provides JSON string deserialization tools.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON formatted string.
    """
    return json.loads(my_str)
