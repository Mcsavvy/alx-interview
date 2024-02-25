#!/usr/bin/python3
"""This module attempts to transpose a matrix"""


def Tmatrix(matrix, start, max_):
    """Helper function that uses recursion to
    transpose a matrix"""
    if start >= max_:
        return
    for i in range(start, max_):
        temp = matrix[start][i]
        matrix[start][i] = matrix[i][start]
        matrix[i][start] = temp
    Tmatrix(matrix, start + 1, max_)


def rotate_2d_matrix(ln):
    """Rotates a n by n matrix by first reversing
    the order of columns then transposing them"""
    count = len(ln)
    for i in range(count):
        j = count - 1
        v = 0
        while j >= v:
            temp = ln[j][i]
            ln[j][i] = ln[v][i]
            ln[v][i] = temp
            v += 1
            j -= 1
    Tmatrix(ln, 0, count)
