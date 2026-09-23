#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Return a copy of a list with one element replaced."""
    new_list = my_list.copy()
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
