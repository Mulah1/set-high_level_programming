#!/usr/bin/python3
"""Defines unittests for square.py."""
import unittest
import os
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    """Represent unittests for the Square class."""

    def setUp(self):
        """Clean up files and reset counter."""
        Base._Base__nb_objects = 0
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_init(self):
        """Test square instantiation and validations."""
        s1 = Square(1)
        self.assertEqual(s1.size, 1)

        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)

        s3 = Square(1, 2, 3)
        self.assertEqual(s3.y, 3)

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

    def test_square_str(self):
        """Test square __str__ method."""
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_square_to_dictionary(self):
        """Test square to_dictionary method."""
        s = Square(10, 2, 1, 1)
        self.assertEqual(s.to_dictionary(), {
            'id': 1, 'size': 10, 'x': 2, 'y': 1
        })

    def test_square_update(self):
        """Test square update method with args and kwargs."""
        s = Square(5, 0, 0, 1)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1)
        self.assertEqual(s.size, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_square_create(self):
        """Test Square.create method."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_square_file_io(self):
        """Test save_to_file and load_from_file for Square."""
        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])

        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])

        s = Square(5)
        Square.save_to_file([s])
        squares = Square.load_from_file()
        self.assertEqual(len(squares), 1)
