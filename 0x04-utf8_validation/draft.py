#!/usr/bin/env python3


def validUTF8(data) -> bool:
    def check_for_8_bits_char(item) -> bool:
        if item < 128:  # 1 bytes character
            return True
        elif item < 192:  # invalid
            return False
        elif 191 < item < 224:  # 2 bytes cahr
            bin_rep = bin(item)[2:]
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
        else:
            bin_rep = bin(item)[2:]
            if bin_rep[5] == '1' and bin_rep[6] == '0':
                return True
            else:
                return False
        return False

    results = list(map(lambda x: check_for_8_bits_char(x), data))

    return all(results)


# def check_for_8_bits_char(item: int) -> bool:
#     """ check for valid 8 bit char

#     Args:
#         item (int): int char

#     Returns:
#         bool: true if less than 127 otherwise fasle
#     """
#     if -127 <= item <= 127:
#         return True
#     else:
#         return False


data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))


# print(type(bin(192)[2:]))
