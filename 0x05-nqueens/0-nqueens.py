#!/usr/bin/python3
"""Importing the sys module """
import sys

""" A program that prints usage and exit"""


def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

""" A function that solves the nqueens program"""

def solve_nqueens(n):
    solutions = []
    board = [-1] * n

    """A function that verifies if a queens position is valid"""


    def is_valid(row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + == col + row:
                 return False
        return True
        """A function that puts the queen is a stated position"""


        def place_queen(row):
            if row == n:
                solution.append([[i, board[i]]] for i in range(n)])
                return
            for col in range(n):
                if is_valid(row, col):
                    board[row] = col
                    place_queen(row + 1)

        place_queen(0)
        return solutions

