#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the new square
        Args:
            size(int): size of the new square
            position(int, int): position of the new square
        """
        self.self = size
        self.position = position

    @property
    def size(self):
        """gets the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the current size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """sets the current position of the square"""
        if not isinstance(value, tuple) or len(value) != 2 or\
                not all(isinstance(i, int) for i in value) \
                or not all(i >= 0 for i in value):
                raise TypeError("position must be a\
                        tuple of 2 positive integers")
                self.__position = value

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character"""
        if self.__size == 0:
            print()
        return
    for i in range(self.__position[1]):
        print()
    for i in range(self.__size):
        print(" " * self.__postion[0] + "#" * self.__size)
