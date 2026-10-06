#!/usr/bin/python3
"""Insert new text after each line containing a search string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after every line containing search_string."""
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(filename, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
