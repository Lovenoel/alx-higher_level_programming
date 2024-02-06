#!/usr/bin/python3
"""A module class BaseGeometry (based on 5-base_geometry.py).
"""


class BaseGeometry:
    """
    Empty class representing a base geometry.

    Methods:
    - area(self): Raises an Exception with the message "area() is
    not implemented."
    """
    def area(self):
        raise Exception("area() is not implemented")
