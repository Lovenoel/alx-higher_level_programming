#!/usr/bin/python3
"""
a class Rectangle that defines a rectangle by:
(based on 4-rectangle.py)
"""


class Rectangle:
    """Represents  a rectangle"""

    def __init__(self, width=0, height=0):
        """initialises a new rectangle
        Args:
            width(int): widthof the rectangle
            height(int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#' characters.
        Returns an empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.__height):
                rectangle += "#" * self.__width
                if i < self.__height - 1:
                    rectangle += "\n"
            return rectangle

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to recreate an instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Destructor method that prints a farewell message
        when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
