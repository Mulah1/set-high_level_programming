#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_regular_list(self):
        """Test with a standard list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the maximum integer at the beginning of the list."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_float_numbers(self):
        """Test with floats."""
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_string_list(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
