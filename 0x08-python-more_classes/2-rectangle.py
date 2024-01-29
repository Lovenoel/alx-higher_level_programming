#!/usr/bin/python3
""" a module that defines a class Rectangle"""


class Rectangle:
    """represents a new rectangle"""
    def __init__(self, width=0, height=0):
        """ Initializes a new rectangle
        Args:
            width(int): the width of the new rectangle
            height(int): the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the new rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width of the new rectanglr"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height of the new rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        "sets the height of the new rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """ returns area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """ returns the perimeterof the rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))
