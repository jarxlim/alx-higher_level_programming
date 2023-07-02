#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This returns the sum of two integers or floats
    
    Args:
        a: first parameter to be passed
        b: second psrameter to be passed
    returns:
        the sum of the two parameters
    Raises:
        TypeError: if neither of the values is an int nor a float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
