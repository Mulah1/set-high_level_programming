#!/usr/bin/python3

def no_c(my_string):
    """Return a string without lowercase or uppercase c characters."""
    result = ""
    for character in my_string:
        if character != 'c' and character != 'C':
            result += character
    return result
