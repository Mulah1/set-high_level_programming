#!/usr/bin/python3
"""Dictionary deletion helper."""


def simple_delete(a_dictionary, key=""):
    """Delete key when present and return the dictionary."""
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
