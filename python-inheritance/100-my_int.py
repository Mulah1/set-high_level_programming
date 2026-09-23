#!/usr/bin/python3
"""Define an integer with inverted equality operators."""


class MyInt(int):
    """An int subclass that rebels against == and !=."""

    def __eq__(self, other):
        """Return the inverse of normal equality."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Return the inverse of normal inequality."""
        return not super().__ne__(other)
