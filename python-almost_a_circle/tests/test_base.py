#!/usr/bin/python3
"""Defines unittests for base.py."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Represent unittests for the Base class."""

    def test_id(self):
        """Test automatic and manual id assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        """Test the static method to_json_string."""
        d = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        json_s = Base.to_json_string([d])
        self.assertIsInstance(json_s, str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        """Test the static method from_json_string."""
        json_s = '[{"id": 1, "width": 2}]'
        list_s = Base.from_json_string(json_s)
        self.assertIsInstance(list_s, list)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
