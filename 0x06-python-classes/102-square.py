#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """represents a square"""
    def __init__(self, size=0):
        """initializes a new square
        Args:
            size(int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """gets the size of the new square"""
        return self._size

    @size.setter
    def size(self, value):
        """sets the size for the new square"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """returns the square area for the new square"""
        return self.size ** 2

    def __eq__(self, other):
        """returns area of the other"""
        return self.area() == other.area()

    def __ne__(self, other):
        """returns area of the other"""
        return self.area() != other.area()

    def __lt__(self, other):
        """returns area of the other"""
        return self.area() < other.area()

    def __le__(self, other):
        """returns area of the other"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """returns area of the other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """returns area of the other"""
        return self.area() >= other.area()
