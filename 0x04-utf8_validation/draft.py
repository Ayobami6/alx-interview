#!/usr/bin/env python3

def validUTF8(data) -> bool:
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

# def check_for_8_bits_char(item: int) -> bool:
#         """ check for valid 8 bit char

#         Args:
#             item (int): int char

#         Returns:
#             bool: true if less than 127 otherwise fasle
#         """
#         if item < 128:  # 1 bytes character
#             return True
#         elif item < 192:  # invalid
#             return False
#         elif 191 < item < 224:  # 2 bytes cahr
#             bin_rep = bin(item)[2:]  # convert to binary
#             if bin_rep[3] == '1' and bin_rep[4] == '0':
#                 return True
#             else:
#                 return False
#         elif 223 < item < 240:  # 3 bytes
#             bin_rep = bin(item)[2:]
#             if bin_rep[4] == '1' and bin_rep[5] == '0':
#                 return True
#             else:
#                 return False
#         elif 239 < item < 248:
#             bin_rep = bin(item)[2:]
#             if bin_rep[5] == '1' and bin_rep[6] == '0':
#                 return True
#             else:
#                 return False
#         return False

#     results = list(map(lambda x: check_for_8_bits_char(x), data))

#     return all(results)

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

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))


# print(type(bin(192)[2:]))
