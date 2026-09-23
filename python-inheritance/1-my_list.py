#!/usr/bin/python3
"""A list subclass with sorted-print functionality."""


class MyList(list):
    """List subclass that can print a sorted copy of itself."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
