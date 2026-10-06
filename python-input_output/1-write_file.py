#!/usr/bin/python3
"""Write string to text file and return number of characters written."""


def write_file(filename="", text=""):
    """Write a text to a file and return the number of written characters."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
