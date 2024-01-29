#!/usr/bin/python3
"""A module of a class Rectangle that defines
a rectangle by: (based on 6-rectangle.py)
"""


class Rectangle:
    """
    Rectangle class defines a rectangle by its width and height.
    """

    # Public class attributes
    number_of_instances = 0  # Counter for the number of instances created
    print_symbol = "#"      # Symbol used for string representation

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with specified width and height.

        Args:
        - width (int): Width of the rectangle (default is 0).
        - height (int): Height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Raises:
        - TypeError: If width is not an integer.
        - ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Raises:
        - TypeError: If height is not an integer.
        - ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            result = 0
        else:
            result = 2 * (self.__width + self.__height)
        return result

    def __str__(self):
        """
        Returns a string representation of the rectangle using print_symbol.

        Returns:
        - str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return (str(self.print_symbol) * self.__width + "\n") * self.__height

    def __repr__(self):
        """
        Returns a string representation of the rectangle for object recreation.

        Returns:
        - str: String representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor method that prints a message when an instance is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
