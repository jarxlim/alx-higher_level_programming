#!/usr/bin/python3
"""module contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises exception when ilts called"""
        raise Exception("area() is not implemented")
