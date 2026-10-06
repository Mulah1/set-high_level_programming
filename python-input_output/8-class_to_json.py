#!/usr/bin/python3
"""Return the dictionary representation of an object for JSON serialization."""


def class_to_json(obj):
    """Return a serializable dictionary for obj."""
    return obj.__dict__
