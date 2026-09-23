#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print each integer in a list in reverse order."""
    for number in reversed(my_list):
        print("{:d}".format(number))
