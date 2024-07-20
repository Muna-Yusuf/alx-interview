#!/usr/bin/python3
"""Defines a function to rotate an n x n 2D matrix 90 degrees
clockwise in place."""


def rotate_2d_matrix(matrix):
    """Rotates an n x n 2D matrix 90 degrees clockwise in place by
    reversing the rows and then transposing the matrix."""
    n = len(matrix)
    matrix.reverse()
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
