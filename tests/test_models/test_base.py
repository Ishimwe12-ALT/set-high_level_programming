#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test Base class functionality."""

    def test_id_auto(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_custom(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 1}]), '[{"id": 1}]')


if __name__ == "__main__":
    unittest.main()
