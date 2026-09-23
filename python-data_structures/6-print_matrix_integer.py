#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        if not row:
            print()
            continue
        for index, number in enumerate(row):
            if index == len(row) - 1:
                print("{:d}".format(number))
            else:
                print("{:d}".format(number), end=" ")
