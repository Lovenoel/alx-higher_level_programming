#!/usr/bin/python3
"""
Class to JSON module
"""


def class_to_json(obj):
    """Return the dictionary description of a class for JSON serialization"""
    return obj.__dict__
