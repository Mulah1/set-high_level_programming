#!/usr/bin/python3
"""Unittests for square.py."""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Represent tests for the Square class."""

    def test_square_instantiation(self):
        """Test square creation."""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)

        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)

        s3 = Square(1, 2, 3)
        self.assertEqual(s3.y, 3)

    def test_square_type_and_value_errors(self):
        """Test type and value validations for square."""
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_square_methods(self):
        """Test str, dictionary, and update methods for square."""
        s = Square(1, 2, 3, 89)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        self.assertEqual(s.to_dictionary(), {'id': 89, 'size': 1, 'x': 2, 'y': 3})

        s.update(10, 5, 6, 7)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)

        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
