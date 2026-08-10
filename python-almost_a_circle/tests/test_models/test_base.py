#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_id_assignment(self):
        """Test automatic and manual id assignment."""
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test to_json_string method."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string(self):
        """Test from_json_string method."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'), [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
