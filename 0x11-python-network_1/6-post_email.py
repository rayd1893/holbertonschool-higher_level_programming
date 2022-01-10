#!/usr/bin/python3
'''Method POST using requests'''
import requests
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    r = requests.post(url, data={'email': argv[2]})
    print(r.text)
