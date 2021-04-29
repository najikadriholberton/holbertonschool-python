#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    result = 0
    for val in argv[1:]:
        result += int(val)
    print(result)
