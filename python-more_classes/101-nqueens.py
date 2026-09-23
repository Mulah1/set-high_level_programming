#!/usr/bin/python3
"""Solve the N queens puzzle using backtracking."""

import sys


def solve_nqueens(size):
    """Print every non-attacking arrangement for a board of size size."""
    solutions = []
    columns = set()
    diagonals = set()
    reverse_diagonals = set()
    placement = []

    def backtrack(row):
        if row == size:
            solutions.append([[index, column]
                              for index, column in enumerate(placement)])
            return
        for column in range(size):
            if (column in columns or row - column in diagonals or
                    row + column in reverse_diagonals):
                continue
            placement.append(column)
            columns.add(column)
            diagonals.add(row - column)
            reverse_diagonals.add(row + column)
            backtrack(row + 1)
            placement.pop()
            columns.remove(column)
            diagonals.remove(row - column)
            reverse_diagonals.remove(row + column)

    backtrack(0)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_nqueens(board_size)
