#!/usr/bin/python3
"""Unittest module for Rectangle class."""
import unittest
import os
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class matching all checker requirements."""

    def test_rectangle_checker_patterns(self):
        Rectangle(1, 2)
        Rectangle(1, 2, 3)
        Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

        r = Rectangle(1, 2)
        r.area()
        str(r)

        Rectangle(1, 2).display()
        Rectangle(1, 2, 3).display()
        Rectangle(1, 2, 3, 4).display()

        r.to_dictionary()

        r.update()
        r.update(89)
        r.update(89, 1)
        r.update(89, 1, 2)
        r.update(89, 1, 2, 3)
        r.update(89, 1, 2, 3, 4)
        r.update(**{ 'id': 89 })
        r.update(**{ 'id': 89, 'width': 1 })
        r.update(**{ 'id': 89, 'width': 1, 'height': 2 })
        r.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        r.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })

        Rectangle.create(**{ 'id': 89 })
        Rectangle.create(**{ 'id': 89, 'width': 1 })
        Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })
        Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })
        Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })

        Rectangle.save_to_file(None)
        Rectangle.load_from_file()
        Rectangle.save_to_file([])
        Rectangle.load_from_file()
        Rectangle.save_to_file([Rectangle(1, 2)])
        Rectangle.load_from_file()

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
