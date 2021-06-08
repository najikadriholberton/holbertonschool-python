#!/usr/bin/python3
"""UTF-8 Validation Module"""


def validUTF8(data):
    """determines if given data is in UTF-8 format"""
    n_bytes = 0

    for num in data:

        byte = format(num, '#010b')[-8:]

        if n_bytes == 0:

            for bit in byte:
                if bit == '0':
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False

        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False

        n_bytes -= 1

    return n_bytes == 0
