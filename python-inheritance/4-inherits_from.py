#!/usr/bin/python3
"""Check whether an object inherits from a specified class."""


def inherits_from(obj, a_class):
    """Return True for a subclass instance, excluding direct instances."""
    return isinstance(obj, a_class) and type(obj) is not a_class
