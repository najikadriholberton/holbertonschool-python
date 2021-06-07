#!/usr/bin/python3
"""Latest 10 commits"""
import requests
from sys import argv

if __name__ == '__main__':
    github_commits = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[1], argv[2])
    r = requests.get(github_commits)
    if "json" not in r.headers.get('content-type'):
        print("not a valid JSON")
    else:
        json = r.json()
        i = 0
        for r in json:
            if i > 9:
                break
            print(r.get('sha') + ': ', end="")
            print(r.get('commit').get('author').get('name'))
            i += 1
