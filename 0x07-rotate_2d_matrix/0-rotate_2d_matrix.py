#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    method to rotate 2D matrix at 90
    """
    # Transpose matrix
    N = len(matrix)
    for row in range(N):
        for col in range(row, N):
            matrix[row][col], matrix[col][row] =\
                matrix[col][row], matrix[row][col]
    # reverse the transposed matrix
    for row in range(N // 2):
        for col in range(N):
            matrix[col][row], matrix[col][N-1-row] =\
                matrix[col][N-1-row], matrix[col][row]
