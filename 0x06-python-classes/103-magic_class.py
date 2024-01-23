#!/usr/bin/python3
"""Python class MagicClass"""
import math


class MagicClass:
    """represents a magic class"""
    def __init__(self, radius=0):
        """intializes the radius"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """returns area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """returns circumference"""
        return 2 * math.pi * self.__radius
