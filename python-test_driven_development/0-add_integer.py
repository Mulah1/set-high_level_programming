#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Return the sum of a and b after casting floats to ints."""
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
