#!/usr/bin/python3
"""Module that indents text after punctuation."""


def text_indentation(text):
    """Print text with blank lines after ., ?, and : characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    lines = [line.strip() for line in result.splitlines()]
    print("\n".join(lines), end="")
