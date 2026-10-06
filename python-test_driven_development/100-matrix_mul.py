#!/usr/bin/python3
"""Module for multiplying matrices."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices and return the result."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    if any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for value in row:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for value in row:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError("m_b should contain only integers or floats")

    row_lengths_a = [len(row) for row in m_a]
    if any(length != row_lengths_a[0] for length in row_lengths_a):
        raise TypeError("each row of m_a must be of the same size")
    row_lengths_b = [len(row) for row in m_b]
    if any(length != row_lengths_b[0] for length in row_lengths_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result
