#!/usr/bin/python3
"""A module of class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""


class BaseGeometry:
    """
    Empty class representing a base geometry.

    Methods:
    - area(self): Raises an Exception with the message "area() is
    not implemented."
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


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.

    Attributes:
    - __width: The width of the rectangle.
    - __height: The height of the rectangle.

    Methods:
    - area(self): Calculates and returns the area of the rectangle.
    - __str__(self): Returns a string representation of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with the given width and height.

        Args:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        - The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        - A string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    Class representing a square.

    Attributes:
    - __size: The size of the square.

    Methods:
    - __init__(self, size): Initializes a square with the given size.
    - area(self): Calculates and returns the area of the square.
    - __str__(self): Returns a string representation of the square.
    """
    def __init__(self, size):
        """
        Initializes a square with the given size.

        Args:
        - size: The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        - A string representation of the square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
