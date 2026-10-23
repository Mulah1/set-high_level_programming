#!/usr/bin/python3
"""Module that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers using binary search."""
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2

        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]

        elif mid < len(list_of_integers) - 1 and list_of_integers[mid + 1] > list_of_integers[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None
