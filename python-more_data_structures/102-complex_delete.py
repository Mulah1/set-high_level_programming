#!/usr/bin/python3
"""Delete dictionary entries matching a value."""


def complex_delete(a_dictionary, value):
    """Return a dictionary without entries whose value matches value."""
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
