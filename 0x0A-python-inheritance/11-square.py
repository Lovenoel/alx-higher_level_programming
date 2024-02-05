#!/usr/bin/python3
"""A module of class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py).
"""


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
        return f"[Square] {self._Rectangle__width}/" \
               f"{self._Rectangle__height}"
