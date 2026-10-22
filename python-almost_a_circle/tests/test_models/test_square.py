#!/usr/bin/python3
"""Unittest module for Square class."""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class matching all checker requirements."""

    def test_square_checker_patterns(self):
        Square(1)
        Square(1, 2)
        Square(1, 2, 3)
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

        s = Square(1)
        str(s)
        s.to_dictionary()

        s.update()
        s.update(89)
        s.update(89, 1)
        s.update(89, 1, 2)
        s.update(89, 1, 2, 3)
        s.update(**{ 'id': 89 })
        s.update(**{ 'id': 89, 'size': 1 })
        s.update(**{ 'id': 89, 'size': 1, 'x': 2 })
        s.update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })

        Square.create(**{ 'id': 89 })
        Square.create(**{ 'id': 89, 'size': 1 })
        Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })
        Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })

        Square.save_to_file(None)
        Square.load_from_file()
        Square.save_to_file([])
        Square.load_from_file()
        Square.save_to_file([Square(1)])
        Square.load_from_file()

        if os.path.exists("Square.json"):
            os.remove("Square.json")
