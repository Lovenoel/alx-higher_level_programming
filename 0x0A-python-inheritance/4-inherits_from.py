#!/usr/bin/python3
"""A module that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
    - obj: The object to be checked.
    - a_class: The specified class.

    Returns:
    - True if the object is an instance of a subclass of the specified class;
      False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
