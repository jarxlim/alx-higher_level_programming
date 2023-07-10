#!/usr/bin/python3
"""module contains fxn that defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """this class represents the base geometry"""

    def area(self):
        """not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """fxn thst validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
