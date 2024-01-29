#!/usr/bin/python3
""" a module that defines a class Rectangle"""


class Rectangle:
    """represents the new rectangle"""
    def __init__(self, width=0, height=0):
        """ Initializes the new rectangle
        Args:
            width(int): the width of the new rectangle
            height(int): the height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the new rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the new rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the new rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of the new rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns an empty string is width or height == 0"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.__height):
                rectangle += "#" * self.__width
                if i < self.__height - 1:
                    rectangle += "\n"
            return rectangle
