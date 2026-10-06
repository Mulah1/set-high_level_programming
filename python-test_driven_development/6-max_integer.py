#!/usr/bin/python3
"""Module to find the maximum integer in a list."""


def max_integer(list=[]):
    """Return the maximum integer from a list."""
    if len(list) == 0:
        return None
    result = list[0]
    for value in list[1:]:
        if value > result:
            result = value
    return result
