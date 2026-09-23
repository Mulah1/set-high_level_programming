#!/usr/bin/python3

def no_c(my_string):
    """Return a string with all lowercase and uppercase c characters removed."""
    result = ""
    for character in my_string:
        if character != 'c' and character != 'C':
            result += character
    return result
