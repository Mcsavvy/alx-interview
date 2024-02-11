#!/usr/bin/python3
"""Island Perimeter."""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid: a 2D array of integers
    Returns: an integer
    """

    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    return perimeter
