#!/usr/bin/python3
"""A module of class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """
    Empty class representing a base geometry.

    Methods:
    - area(self): Raises an Exception with the message "area()
    is not implemented."
    - integer_validator(self, name, value): Validates the value as an integer.
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.

        Args:
        - name: The name of the value.
        - value: The value to be validated.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
        - str: A string representation.
        """
        return "[Exception] area() is not implemented"
