#!/usr/bin/python3
'''Control errors using requests'''
from sys import argv
import requests


if __name__ == '__main__':
    r = requests.get(argv[1])
    code = r.status_code
    if code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
