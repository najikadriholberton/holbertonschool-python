#!/usr/bin/python3
"""Error Code"""
from urllib import request, error, parse
from sys import argv


if __name__ == '__main__':
    r = request.Request(argv[1])
    try:
        with request.urlopen(r) as response:
            html = response.read()
            print(html.decode('utf8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
