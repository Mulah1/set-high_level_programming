#!/usr/bin/python3
"""Module to print a square with '#'."""


def print_square(size):
    """Print a square of '#' characters of side length size."""
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
