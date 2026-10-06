#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Return the sum of two integers after coercing floats to ints."""
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(b, bool) or not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
