#!/usr/bin/python3
"""Post Email"""
from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    v = {}
    v['email'] = argv[2]
    d = parse.urlencode(v)
    d = d.encode('ascii')
    r = request.Request(argv[1], d)
    with request.urlopen(r) as response:
        html = response.read()
        print(html.decode('utf8'))
