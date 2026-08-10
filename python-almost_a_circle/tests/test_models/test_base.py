#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_base_auto_id(self):
        """Test Base() for assigning automatically an ID."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_base_auto_id_increment(self):
        """Test Base() for assigning automatically an ID + 1 of previous."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_custom_id(self):
        """Test Base(89) saving the ID passed."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test Base.to_json_string(None)."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test Base.to_json_string([])."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dict(self):
        """Test Base.to_json_string([{'id': 12}])."""
        d = [{'id': 12}]
        self.assertEqual(Base.to_json_string(d), '[{"id": 12}]')

    def test_to_json_string_return_type(self):
        """Test Base.to_json_string returning a string."""
        d = [{'id': 12}]
        self.assertIsInstance(Base.to_json_string(d), str)

    def test_from_json_string_none(self):
        """Test Base.from_json_string(None)."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test Base.from_json_string("")."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_valid(self):
        """Test Base.from_json_string('[{"id": 89}]')."""
        s = '[{"id": 89}]'
        self.assertEqual(Base.from_json_string(s), [{'id': 89}])

    def test_from_json_string_return_type(self):
        """Test Base.from_json_string returning a list."""
        s = '[{"id": 89}]'
        self.assertIsInstance(Base.from_json_string(s), list)


if __name__ == '__main__':
    unittest.main()
