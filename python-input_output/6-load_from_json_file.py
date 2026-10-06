#!/usr/bin/python3
"""Load an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Read a JSON file and return the Python object it represents."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
