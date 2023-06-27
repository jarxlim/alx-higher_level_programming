#!/usr/bin/python3
"""Doc for a class Square."""


class Square:
    """Represent a square class."""

    def __init__(self, size=0):
        """Initializes a new Square.
        Args:
            size (int): size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
