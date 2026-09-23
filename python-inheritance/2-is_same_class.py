#!/usr/bin/python3
"""Check whether an object exactly matches a class."""


def is_same_class(obj, a_class):
    """Return True only when obj's exact class is a_class."""
    return type(obj) is a_class
