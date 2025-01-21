#!/usr/bin/python3
"""
Program that solves the N queens problem.
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board: board
        row: rows
        col: column

    Returns: numbers
    """
    for i in range(row):
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(n, row=0, board=None):
    """
    Solve the N-Queens problem using backtracking.

    Args:
        n: numberss
        row: rows
        board: boards
    Returns: numbers
    """
    if board is None:
        board = []

    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            solve_nqueens(n, row + 1, board + [col])


def nqueens(N):
    """
    Handle user input and validate it.

    Args:
        N: parameter

    Returns: numbers
    """
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


def main():
    """
    Main function to handle command-line arguments.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])


if __name__ == "__main__":
    main()
