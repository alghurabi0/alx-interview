#!/usr/bin/python3
""" island perimeter problem """


def countSides(grid, i, j) -> int:
    """ counting sides """
    count = 0
    if i > 0:
        if grid[j][i-1] == 0:
            count += 1
    else:
        count += 1

    if i < len(grid[j]) - 1:
        if grid[j][i+1] == 0:
            count += 1
    else:
        count += 1

    if j > 0:
        if grid[j-1][i] == 0:
            count += 1
    else:
        count += 1

    if j < len(grid) - 1:
        if grid[j+1][i] == 0:
            count += 1
    else:
        count += 1

    return count


def island_perimeter(grid):
    """ island perimeter problem """
    count = 0
    for j, row in enumerate(grid):
        for i, num in enumerate(row):
            if num == 1:
                count += countSides(grid, i, j)
    return count
