#!/usr/bin/python3
"""Replace matching values in a list."""


def search_replace(my_list, search, replace):
    """Return a new list with every occurrence of search replaced."""
    return [replace if value == search else value for value in my_list]
