#!/usr/bin/python3
"""
The module contains a function that multiplies 2 matrices

"""


def matrix_mul(m_a, m_b):
    """This function multiplies 2 matrices

    Args:
        m_a: list of lists of int/float)
        m_b: list of lists of int/float)

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: If m_a or m_b is not a list of lists
        TypeError: If one element of list of lists is not int/float
        TypeError: If row of m_a or m_b are not the same size
        ValueError: If m_a or m_b is empty
        ValueError: If m_a and m_b cannot be multiplied

    Returns:
        A new list which is the resilt of the multiplication

    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_a for number in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(element, int) or isinstance(element, float))
               for element in [number for row in m_b for number in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix01 = []
    for i in range(len(m_b[0])):
        rows = []
        for j in range(len(m_b)):
            rows.append(m_b[j][i])
        matrix01.append(rows)

    matrix02 = []
    for row in m_a:
        rows = []
        for column in matrix01:
            res = 0
            for p in range(len(matrix01[0])):
                res += row[p] * column[p]
            rows.append(res)
        matrix02.append(rows)

    return matrix02
