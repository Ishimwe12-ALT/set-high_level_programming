#!/usr/bin/python3
"""Unittest for Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_instantiation(self):
        """Test instantiation and attribute assignment."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.id, 12)

    def test_validations(self):
        """Test type and value errors."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")


if __name__ == '__main__':
    unittest.main()
