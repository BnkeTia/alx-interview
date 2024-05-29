#!/usr/bin/python3
"""A program to solve the N queens puzzle."""

import sys


def print_usage_and_exit():
    """Prints usage message and exits."""
    print("Usage: nqueens N")
    sys.exit(1)


def solve_nqueens(n):
    """Solves the N queens puzzle and returns all solutions."""
    solutions = []
    board = [-1] * n

    def is_valid(row, col):
        """Checks if a queen can be placed at (row, col) without attacks"""
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def place_queen(row):
        """Places queens on the board using backtracking."""
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                place_queen(row + 1)

    place_queen(0)
    return solutions


def main():
    """Entry point for the N queens solution."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
