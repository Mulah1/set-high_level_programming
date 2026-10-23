#!/usr/bin/python3
"""Module that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers."""
    if not list_of_integers:
        return None
    nums = list_of_integers
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return nums[low]
