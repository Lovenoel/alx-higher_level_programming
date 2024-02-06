#!/usr/bin/python3
"""A module that returns the list of available attributes and methods
of an object:
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
    - obj: The object for which attributes and methods are to be looked up.

    Returns:
    - A list containing the names of attributes and methods of the object.
    """
    return dir(obj)
