#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """overrides == with !="""
        return int(self) == other
