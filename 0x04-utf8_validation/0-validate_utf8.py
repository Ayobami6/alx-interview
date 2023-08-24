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
        if item < 128:  # 1 byte character
            return True
        elif 192 <= item < 224:  # 2 bytes character
            # check for the continuation byte rules
            return 128 <= data[i + 1] < 192 if i + 1 < len(data) else False
        elif 224 <= item < 240:  # 3 bytes character
            return (
                128 <= data[i + 1] < 192
                and 128 <= data[i + 2] < 192
                if i + 2 < len(data)
                else False
            )
        elif 240 <= item < 248:  # 4 bytes character
            return (
                128 <= data[i + 1] < 192
                and 128 <= data[i + 2] < 192
                and 128 <= data[i + 3] < 192
                if i + 3 < len(data)
                else False
            )
        return False

    i = 0
    while i < len(data):
        if not check_for_8_bits_char(data[i]):
            return False
        i += 1

    return True
