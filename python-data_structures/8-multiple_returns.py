#!/usr/bin/python3

def multiple_returns(sentence):
    """Return a tuple with the length and first character of a string."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
