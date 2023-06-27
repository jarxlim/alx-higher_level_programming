#!/usr/bin/python3
"""define a magicclass matching"""
import math


class MagicClass:
    """represent a circle"""

    def __init__(self, radius=0):
        """ write a docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ defines area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """ define circumference"""
        return 2 * math.pi * self.__radius
