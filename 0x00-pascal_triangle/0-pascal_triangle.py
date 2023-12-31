#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n: int):
    """Generate a Pascal's triangle of `n`

    Args:
        n: an integer
    Return:
        a list of lists of integers
    """

    def get_row(prev: 'list[int]'):
        """get a row in the triangle"""
        row = [1]
        # noticed a pattern when the length of the next row
        # is always the length of the previous + 1
        num_of_loops = len(prev) - 1
        for i in range(num_of_loops):
            row.append(prev[i] + prev[i + 1])
        row.append(1)
        return row

    triangle = [[1]]

    # base case
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    row = triangle[0]
    for x in range(1, n):
        row = get_row(row)
        triangle.append(row)
    return triangle
