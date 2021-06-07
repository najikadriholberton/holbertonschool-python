#!/usr/bin/python3
"""Get URL using urllib"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('    - type: ' + str(type(html)))
        print('    - content: ' + str(html))
        print('    - utf8 content: ' + str(html.decode('utf-8')))
