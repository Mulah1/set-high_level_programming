#!/usr/bin/python3
"""Set symmetric difference helper."""


def only_diff_elements(set_1, set_2):
    """Return elements present in exactly one of the sets."""
    return set_1 ^ set_2
