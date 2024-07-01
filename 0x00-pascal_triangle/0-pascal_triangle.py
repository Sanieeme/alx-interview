#!/usr/bin/python3
""" returns a list of lists of integers """


def pascal_triangle(n):
    if n <= 0:
        return []
    t = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(t[i-1][j-1] + t[i-1][j])
        row.append(1)
        t.append(row)
    return t
