#!/usr/bin/python3
"""Module that writes formatted text with guided line breaks."""


def text_indentation(text):
    """Print text with blank lines after ., ?, and :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = []
    current = []

    for char in text:
        current.append(char)
        if char in ".?:":
            line = "".join(current).strip()
            if line:
                lines.append(line)
            lines.append("")
            current = []

    if current:
        line = "".join(current).strip()
        if line:
            lines.append(line)

    print("\n\n".join(lines), end="")
