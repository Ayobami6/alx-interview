#!/usr/bin/python3
""" check for valid utf8 module
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Summary

    Args:
        data (List[int]): list of integers

    Returns:
        bool: true if a valid utf-8 otherwise false
    """
    i = 0
    while i < len(data):
        if data[i] < 128:  # Single-byte character
            i += 1
        elif 192 <= data[i] < 224:  # Two-byte character
            if i + 1 >= len(data) or not (128 <= data[i + 1] < 192):
                return False
            i += 2
        elif 224 <= data[i] < 240:  # Three-byte character
            if (
                i + 2 >= len(data)
                or not (128 <= data[i + 1] < 192)
                or not (128 <= data[i + 2] < 192)
            ):
                return False
            i += 3
        elif 240 <= data[i] < 248:  # Four-byte character
            if (
                i + 3 >= len(data)
                or not (128 <= data[i + 1] < 192)
                or not (128 <= data[i + 2] < 192)
                or not (128 <= data[i + 3] < 192)
            ):
                return False
            i += 4
        else:
            return False
    return True
