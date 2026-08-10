#!/usr/bin/python3
"""Unittest for Square class."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_attributes_and_area(self):
        """Test initialization, property getter/setter, and area."""
        s = Square(5, 1, 2, 7)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.area(), 25)

    def test_size_setter_validation(self):
        """Test validation on size setter."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "invalid"
        with self.assertRaises(ValueError):
            s.size = -5

    def test_str(self):
        """Test __str__ representation for Square."""
        s = Square(5, 2, 1, 3)
        self.assertEqual(str(s), "[Square] (3) 2/1 - 5")


if __name__ == '__main__':
    unittest.main()
