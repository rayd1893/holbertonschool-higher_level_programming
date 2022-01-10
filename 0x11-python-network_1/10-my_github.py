#!/usr/bin/python3
'''Using GitHub API'''
from sys import argv
import requests
from requests.models import Response


if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    r = requests.get('https://api.github.com/user', auth=(user, password))
    if r.status_code == 200:
        res = r.json()
        print(res.get('id'))
    else:
        print('None')
