#!/usr/bin/python3
"""JSON API"""
import requests
from sys import argv


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        r = requests.post(url, data={'q': argv[1]})
    else:
        r = requests.post(url, data={'q': ""})

    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except BaseException:
        print("Not a valid JSON")
