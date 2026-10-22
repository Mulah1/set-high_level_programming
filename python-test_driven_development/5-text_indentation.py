#!/usr/bin/python3
"""
Defines a text indentation function.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for i, c in enumerate(text):
        if flag == 0:
            if c == ' ':
                continue
            flag = 1
        if flag == 1:
            if c in ".?:":
                print(c, end="")
                if i + 1 < len(text):
                    print("\n\n", end="")
                flag = 2
            else:
                print(c, end="")
        elif flag == 2:
            if c == ' ':
                continue
            flag = 1
            print(c, end="")
