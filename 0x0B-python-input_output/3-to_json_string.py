#!/usr/bin/python3
"""
To JSON String module
"""


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)"""
    import json
    return json.dumps(my_obj)
