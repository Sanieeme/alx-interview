#!/usr/bin/python3
""" function"""


def island_perimeter(grid):
    """function that returns the perimeter of the island
    """
    if not grid or not grid[0]:
        return 0

    peri = 0
    row = len(grid)
    col = len(grid[0])

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    peri += 1
                if i == row-1 or grid[i+1][j] == 0:
                    peri += 1
                if j == 0 or grid[i][j-1] == 0:
                    peri += 1
                if j == col-1 or grid[i][j+1] == 0:
                    peri += 1
    return peri
