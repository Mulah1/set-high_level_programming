#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Return a list with True if each element is divisible by 2."""
    result = []
    for number in my_list:
        if number % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
