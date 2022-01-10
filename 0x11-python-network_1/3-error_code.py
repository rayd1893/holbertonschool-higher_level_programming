#!/usr/bin/python3
'''HTTPError  with urllib'''
import urllib.request
import urllib.error
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
