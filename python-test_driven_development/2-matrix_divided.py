#!/usr/bin/python3
"""Module for dividing a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number."""
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) == 0 for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    first_row_len = len(matrix[0])
    if any(len(row) != first_row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if isinstance(div, bool) or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            new_row.append(round(value / div, 2))
        result.append(new_row)
    return result
