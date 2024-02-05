#!/usr/bin/python3
"""A module that returns True if the object is an instance of, or if the
object is an instance of a class that inherited from, the specified class;
otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class; otherwise
    False.

    Args:
    - obj: The object to be checked.
    - a_class: The specified class.

    Returns:
    - True if the object is an instance of, or if the object is an instance
      of a class that inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
