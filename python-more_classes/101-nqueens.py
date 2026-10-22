#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys

if __name__ == "__main__":
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

    def solve(row, cols, diagonals1, diagonals2, placement):
        if row == n:
            result = [[r, c] for r, c in enumerate(placement)]
            print(result)
            return

        for col in range(n):
            if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue
            cols.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)
            placement.append(col)

            solve(row + 1, cols, diagonals1, diagonals2, placement)

            placement.pop()
            cols.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    solve(0, set(), set(), set(), [])
