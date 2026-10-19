#!/usr/bin/python3
"""Defines unittests for base.py."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Represent unittests for the Base class."""

    def setUp(self):
        """Reset nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_base_id(self):
        """Test automatic ID assignment and incrementing."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_id_saved(self):
        """Test custom ID passed to Base."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dict(self):
        """Test to_json_string with a dictionary list and return type."""
        d = [{'id': 12}]
        res = Base.to_json_string(d)
        self.assertIsInstance(res, str)
        self.assertEqual(res, '[{"id": 12}]')

    def test_from_json_string_none(self):
        """Test from_json_string with None or empty."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_data(self):
        """Test from_json_string with JSON string and return type."""
        json_s = '[{"id": 89}]'
        res = Base.from_json_string(json_s)
        self.assertIsInstance(res, list)
        self.assertEqual(res, [{'id': 89}])
