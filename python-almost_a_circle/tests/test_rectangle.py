#!/usr/bin/python3
"""Defines unittests for rectangle.py."""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Represent unittests for the Rectangle class."""

    def setUp(self):
        """Clean up files and reset counter."""
        Base._Base__nb_objects = 0
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_rectangle_init(self):
        """Test rectangle instantiation with various arguments."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.x, 3)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)

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

    def test_rectangle_area(self):
        """Test rectangle area method."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_rectangle_str(self):
        """Test rectangle __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_rectangle_display(self):
        """Test rectangle display methods."""
        r1 = Rectangle(2, 2)
        r1.display()
        r2 = Rectangle(2, 2, 1, 0)
        r2.display()
        r3 = Rectangle(2, 2, 1, 1)
        r3.display()

    def test_rectangle_to_dictionary(self):
        """Test rectangle to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r.to_dictionary(), {
            'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9
        })

    def test_rectangle_update(self):
        """Test rectangle update method with args and kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1)
        self.assertEqual(r.width, 1)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_rectangle_create(self):
        """Test Rectangle.create method."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_rectangle_file_io(self):
        """Test save_to_file and load_from_file for Rectangle."""
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])

        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 1)
