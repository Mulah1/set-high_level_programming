#!/usr/bin/python3
"""Generate Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle as a list of lists."""
    if n <= 0:
        return []

    triangle = []
    for row_index in range(n):
        row = [1]
        if row_index > 0:
            previous = triangle[row_index - 1]
            for col in range(1, row_index):
                row.append(previous[col - 1] + previous[col])
            row.append(1)
        triangle.append(row)
    return triangle
