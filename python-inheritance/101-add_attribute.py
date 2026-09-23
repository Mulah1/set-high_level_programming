#!/usr/bin/python3
"""Add attributes to objects that support instance attributes."""


def add_attribute(obj, attribute, value):
    """Add an attribute, or raise TypeError when the object cannot do so."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
