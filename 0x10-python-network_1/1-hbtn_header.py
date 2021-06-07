#!/usr/bin/python3
"""Response Header X-Request-Id"""
from urllib import request
from sys import argv


if __name__ == '__main__':
    with request.urlopen(argv[1]) as response:
        header = response.info()
        print(header.get("X-Request-Id"))
