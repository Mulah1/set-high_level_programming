#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print each integer in a list in reverse order."""
    if my_list is None:
        return
    for number in reversed(my_list):
        print("{:d}".format(number))
