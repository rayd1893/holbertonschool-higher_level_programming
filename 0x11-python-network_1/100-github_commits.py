#!/usr/bin/python3
'''List commits using GitHub API'''
from sys import argv
import requests
from requests.models import Response


if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits?per_page=10'
    r = requests.get(url.format(owner, repo))
    data = r.json()
    for i in data:
        print('{}: {}'.format(
            i.get('sha'), i.get('commit').get('author').get('name')))
