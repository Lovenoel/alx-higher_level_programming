#!/usr/bin/python3
"""A module a function that adds a new attribute to an object if it’s
possible
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Raises a TypeError exception if the object cannot have a new attribute.

    Args:
    - obj: The object to which the attribute should be added.
    - attribute: The name of the new attribute.
    - value: The value to be assigned to the new attribute.

    Raises:
    - TypeError: If the object cannot have a new attribute.
    """
    if hasattr(obj, "__dict__") \
            or (hasattr(type(obj), "__slots__") and attribute in type(obj).__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
