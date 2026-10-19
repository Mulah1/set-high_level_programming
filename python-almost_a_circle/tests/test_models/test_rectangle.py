#!/usr/bin/python3
"""Unittests for rectangle.py."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Represent tests for the Rectangle class."""

    def test_rectangle_instantiation(self):
        """Test rectangle creation with valid parameters."""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

        r2 = Rectangle(1, 2, 3)
        self.assertEqual(r2.x, 3)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.y, 4)

    def test_rectangle_type_errors(self):
        """Test type errors for invalid inputs."""
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

    def test_rectangle_value_errors(self):
        """Test value errors for invalid numbers."""
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

    def test_rectangle_methods(self):
        """Test area, str, display, and dictionary methods."""
        r = Rectangle(3, 2, 0, 0, 1)
        self.assertEqual(r.area(), 6)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 3/2")
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 3, 'height': 2, 'x': 0, 'y': 0})

    def test_rectangle_update(self):
        """Test update methods with args and kwargs."""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.id, 89)

    def file_operations(self):
        """Test save and load files."""
        r = Rectangle(1, 2, id=1)
        Rectangle.save_to_file([r])
        rects = Rectangle.load_from_file()
        self.assertEqual(len(rects), 1)
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
