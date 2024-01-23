#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """rEpresents a square"""

    def __init__(self, size=0):
        """Intializes a new square
        Args:
            size(int): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private instance attribute

    def area(self):
        return self.__size ** 2
