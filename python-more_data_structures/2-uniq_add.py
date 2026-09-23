#!/usr/bin/python3
"""Add unique integers from a list."""


def uniq_add(my_list=[]):
    """Return the sum of each distinct value in my_list."""
    return sum(set(my_list))
