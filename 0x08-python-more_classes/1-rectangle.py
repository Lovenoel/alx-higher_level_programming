#!/usr/bin/python3
"""a module that defines a class Rectangle"""


class Rectangle:
    """Represents a new rectangle"""
    def __init__(self, width=0, height=0):
        """ Initializes a new rectangle
        Args:
            width(int): width of the new rectangle
            height(in): height of the new rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """gets the height of the new rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height of the new rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """gets the width of the new rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width of the new rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
