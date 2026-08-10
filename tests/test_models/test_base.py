#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_id_auto(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_auto_increment(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_custom(self):
        b = Base(89)
        self.assertEqual(b.id, 89)


if __name__ == "__main__":
    unittest.main()
