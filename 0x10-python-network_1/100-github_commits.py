#!/usr/bin/python3
"""Latest 10 commits"""
import requests
from sys import argv

if __name__ == '__main__':
    github_commits = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[1], argv[2])
    r = requests.get(github_commits)
    commits = r.json()
    for i in commits[:10]:
        print(i.get('sha'), end=': ')
        print(i.get('commit').get('author').get('name'))
