#!/usr/bin/python3
"""Error Code Requests"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    if int(r.status_code) < 400:
        print(r.text)
    else:
        print("Error code: " + str(r.status_code))
