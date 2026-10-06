#!/usr/bin/python3
"""Module for multiplying matrices using NumPy."""

try:
    import numpy as np
except ImportError:
    np = None


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    if np is None:
        raise ImportError("NumPy is required for lazy_matrix_mul")
    return np.matmul(m_a, m_b)
