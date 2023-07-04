#!/usr/bin/python3

"""This module contains a function that multiplies two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplication of two matrices.
    Args:
        m_a: list of lists of ints/floats.
        m_b: list of lists of ints/floats.
    """

    return (np.matmul(m_a, m_b))
