#!/usr/bin/python3
""" Rotate 2D matrix
"""
from typing import List


def rotate_2d_matrix(matrix: List[list]) -> None:
    """ Rotate 2D matrix 0 degrees clockwise

    Args:
        matrix (List[list]): 2D matrix
    """
    n: int = len(matrix)
    temp: list = []
    tmp: List[list] = list(matrix)
    for i in range(n):
        for j in range(n - 1, -1, -1):
            temp.append(tmp[j][i])
        matrix[i] = temp
        temp = []
