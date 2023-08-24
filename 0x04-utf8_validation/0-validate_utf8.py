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
        if item < 128:  # 1 bytes character
            return True
        elif item < 192:  # invalid
            return False
        elif 191 < item < 224:  # 2 bytes cahr
            bin_rep = bin(item)[2:]  # convert to binary
            if bin_rep[3] == '1' and bin_rep[4] == '0':
                return True
            else:
                return False
        elif 223 < item < 240:  # 3 bytes
            bin_rep = bin(item)[2:]
            if bin_rep[4] == '1' and bin_rep[5] == '0':
                return True
            else:
                return False
        elif 239 < item < 248:
            bin_rep = bin(item)[2:]
            if bin_rep[5] == '1' and bin_rep[6] == '0':
                return True
            else:
                return False
        return False

    results = list(map(lambda x: check_for_8_bits_char(x), data))

    return all(results)
