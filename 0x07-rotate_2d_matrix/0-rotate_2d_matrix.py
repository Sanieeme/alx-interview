#!/usr/bin/env python3
""" """


def rotate_2d_matrix(matrix):
    """method that do not return anything"""
    N = len(matrix)
    for n in range(0, int(N / 2)):
        for m in range(n, N- n - 1):
            temp = matrix[n][m]
            matrix[n][m] = matrix[N - 1 - m][n]
            matrix[N - 1 - m][n] = matrix[N - 1 - n][N - 1 - m]
            matrix[N - 1 - n][N - 1 - m] = matrix[m][N - 1 - n]
            matrix[m][N - 1 - n] = temp
