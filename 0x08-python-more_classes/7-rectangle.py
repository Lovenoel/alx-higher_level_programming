#!/usr/bin/python3
""" a module that defines a class rectangle"""


class Rectangle:
    """ represents new rectangle"""
    number_of_instances = 0  # Public class attribute initialized to 0
    print_symbol = "#"  """ Public class attribute for
                        print_symbol initialized to #
                        """

    def __init__(self, width=0, height=0):
        """ intializes new rectangle
        Args:
            width(int): width
            height(int): height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def perimeter(self):
        """ returns perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for i in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width
                if i < self.__height - 1:
                    rectangle += "\n"
            return rectangle

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1  # Decrement
        print("Bye rectangle...")
