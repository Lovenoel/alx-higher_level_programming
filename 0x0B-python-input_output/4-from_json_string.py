#!/usr/bin/python3
"""
From JSON string to object module
"""


def from_json_string(my_str):
    """Return an object represented by a JSON string"""
    import json
    return json.loads(my_str)
