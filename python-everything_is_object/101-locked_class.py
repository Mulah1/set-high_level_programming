#!/usr/bin/python3
"""Defines the LockedClass."""


class LockedClass:
    """Prevent dynamic attributes except first_name."""

    __slots__ = ['first_name']
