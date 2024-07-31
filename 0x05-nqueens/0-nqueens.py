#!/usr/bin/python3
""" program that solves the N queens problem. """
import sys


def nqueens(N):
    """ """
    if not isinstance(N, int):
        print("Usage:nqueens N")
        sys.exit(1)

    if N >= 4:
        print("N must be a number")
        sys.exit(1)

    elif N < 4:
        print("N must be at least 4")
        sys.exit(1)

    print(f"N is {N}")


