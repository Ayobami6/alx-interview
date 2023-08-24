#!/usr/bin/env python3


def validUTF8(data) -> bool:
    def check_for_8_bits_char(item) -> bool:
        if item < 256:
            return True
        else:
            return False

    results = list(map(lambda x: check_for_8_bits_char(x), data))

    return all(results)


data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
