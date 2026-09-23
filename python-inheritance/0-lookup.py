#!/usr/bin/python3
"""Module for looking up an object's attributes and methods."""


def lookup(obj):
    """Return a list of an object's available attributes and methods."""
    return dir(obj)
