#!/usr/bin/python3
"""
Module for matrix_divided method.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    """
    err_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"
    err_div = "div must be a number"
    err_zero = "division by zero"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_matrix)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(err_matrix)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(err_size)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(err_matrix)

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError(err_div)

    if div == 0:
        raise ZeroDivisionError(err_zero)

    return [[round(x / div, 2) for x in row] for row in matrix]
