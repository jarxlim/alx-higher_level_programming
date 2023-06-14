#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for column in matrix:
        return [list(map(lambda x: x**2, column))
