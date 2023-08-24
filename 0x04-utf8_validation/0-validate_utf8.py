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
    def check_for_8_bits_char(item: int) -> bool:
        """ check for valid 8 bit char

        Args:
            item (int): int char

        Returns:
            bool: true if less than 127 otherwise fasle
        """
        if item < 256:
            return True
        else:
            return False

    results = list(map(lambda x: check_for_8_bits_char(x), data))

    return all(results)
