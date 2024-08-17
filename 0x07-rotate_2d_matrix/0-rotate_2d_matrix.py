#!/usr/bin/python3
"""function """


def rotate_2d_matrix(matrix):
    """method that  rotate it 90 degrees clockwise
    """
    N = len(matrix)
    for n in range(N):
        for m in range(n + 1, N):
            matrix[n][m], matrix[m][n] = matrix[m][n], matrix[n][m]

    for n in range(N):
        matrix[n].reverse()
