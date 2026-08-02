#!/usr/bin/python3
"""
This module provides tools to load Python objects from JSON files.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a specified JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
