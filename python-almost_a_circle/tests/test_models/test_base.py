#!/usr/bin/python3
"""Unittests for base.py."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase.TestCase if hasattr(unittest, 'TestCase') else unittest.TestCase):
    """Represent tests for the Base class."""

    def test_base_id(self):
        """Test automatic and manual ID assignments."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test to_json_string static method."""
        d = [{'id': 12}]
        json_s = Base.to_json_string(d)
        self.assertIsInstance(json_s, str)
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(json_s, '[{"id": 12}]')

    def test_from_json_string(self):
        """Test from_json_string static method."""
        json_s = '[{"id": 89}]'
        list_s = Base.from_json_string(json_s)
        self.assertIsInstance(list_s, list)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(list_s, [{'id': 89}])
