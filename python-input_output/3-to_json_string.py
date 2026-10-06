#!/usr/bin/python3
"""Return the JSON representation of an object."""

import json


def to_json_string(my_obj):
    """Convert an object to its JSON string representation."""
    return json.dumps(my_obj)
