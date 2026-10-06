#!/usr/bin/python3
"""Append a string to a file and return the number of characters added."""


def append_write(filename="", text=""):
    """Append text to a file and return how many characters were added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
