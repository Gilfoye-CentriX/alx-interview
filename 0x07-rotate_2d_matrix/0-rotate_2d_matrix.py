#!/usr/bin/python3
"""2D matrix rotation module.
"""

def rotate_2d_matrix(matrix):
    n = len(matrix)
    
    """ Transpose the matrix
    """
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = matrix[i][j]
    
    """Reverse each row to rotate 90 degrees clockwise
    """
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]

    """Output the rotated matrix in the desired format
    """
    """
    print('[')
    for row in matrix:
        print(f'    {row},')
    print(']')
"""
