#!/usr/bin/python3
'''This module contains function that prints a square with the character #'''


def print_square(size):
    '''
    function that prints a square

    Args:
        size: size length of the square

    Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size > 0:
        print(('#' * size + '\n') * size, end='')
