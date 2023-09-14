#!/usr/bin/python3
""" Rotate 2D matrix
"""


def rotate_2d_matrix(matrix: list) -> None:
    """ Rotate 2D matrix 0 degrees clockwise

    Args:
        matrix (List[list]): 2D matrix
    """
    n: int = len(matrix)
    temp: list = []
    tmp: list = list(matrix)
    for i in range(n):
        for j in range(n - 1, -1, -1):
            temp.append(tmp[j][i])
        matrix[i] = temp
        temp = []
