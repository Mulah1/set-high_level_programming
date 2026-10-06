#!/usr/bin/python3
"""Unit tests for max_integer."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_item(self):
        self.assertEqual(max_integer([7]), 7)

    def test_basic_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_positive(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -2, -5]), -2)

    def test_mixed_values(self):
        self.assertEqual(max_integer([0, -1, 9, 3]), 9)


if __name__ == "__main__":
    unittest.main()
