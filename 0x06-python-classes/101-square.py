#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes a new square
        Args:
            size(int): size of the new square
            position(int): position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets the size of the new square"""
        return self._size

    @size.setter
    def size(self, value):
        """sets the size of the new square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """gets the position of the new square"""
        return self._position

    @position.setter
    def position(self, value):
        """sets the position for the new square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """returns the square area of the new square"""
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
