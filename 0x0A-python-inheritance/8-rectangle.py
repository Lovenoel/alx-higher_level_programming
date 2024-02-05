#!usr/bin/python3
"""A module of class Rectangle that inherits from BaseGeometry
(7-base_geometry.py).
"""


class BaseGeometry:
    """
    Class representing a base geometry.

    Methods:
    - area(self): Raises an Exception with the message "area() is
    not implemented."
    - integer_validator(self, name, value): Validates the value as an integer.
    """
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented."
        """
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


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.

    Attributes:
    - __width: The width of the rectangle.
    - __height: The height of the rectangle.

    Methods:
    - __init__(self, width, height): Initializes a rectangle with
    the given width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.

        Args:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        - A string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
