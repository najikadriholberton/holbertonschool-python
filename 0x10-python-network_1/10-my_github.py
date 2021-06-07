#!/usr/bin/python3
"""use API to do basic authentication on Github"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if "json" not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        json = r.json()
        print(json.get('id'))
