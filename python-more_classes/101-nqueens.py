#!/usr/bin/python3
"""
This module solves the N queens puzzle using a backtracking algorithm.
"""

import sys


def is_safe(queens, row, col):
    """
    Check if a queen can be placed at a given position.

    Args:
        queens (list): List of column positions for placed queens.
        row (int): Current row index.
        col (int): Column index to test.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    for r in range(row):
        if queens[r] == col:
            return False
        if abs(queens[r] - col) == abs(r - row):
            return False
    return True


def solve_nqueens(n, row, queens, solutions):
    """
    Recursively solve the N queens problem using backtracking.

    Args:
        n (int): Size of the chessboard.
        row (int): Current row to place a queen.
        queens (list): Current queen positions.
        solutions (list): List to store valid solutions.
    """
    if row == n:
        solution = []
        for r in range(n):
            solution.append([r, queens[r]])
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(queens, row, col):
            queens[row] = col
            solve_nqueens(n, row + 1, queens, solutions)


def main():
    """
    Parse arguments and print all solutions to the N queens problem.
    """
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

    queens = [-1] * n
    solutions = []

    solve_nqueens(n, 0, queens, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
