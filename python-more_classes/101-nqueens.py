#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys


def solve_nqueens():
    """Validates inputs and runs the N queens solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        """Checks if a queen can be placed at board[row][col]."""
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row, board):
        """Recursively finds all valid placements for queens."""
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            print(solution)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)

    backtrack(0, [-1] * n)


if __name__ == "__main__":
    solve_nqueens()
