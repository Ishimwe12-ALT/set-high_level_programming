#!/usr/bin/python3
"""Unittest for Rectangle class."""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def test_attributes_and_area(self):
        """Test initialization, properties, and area calculation."""
        r = Rectangle(10, 2, 1, 1, 99)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 99)
        self.assertEqual(r.area(), 20)

    def test_validations(self):
        """Test type and value errors for dimensions and coordinates."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "1")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_str(self):
        """Test __str__ representation."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == '__main__':
    unittest.main()
