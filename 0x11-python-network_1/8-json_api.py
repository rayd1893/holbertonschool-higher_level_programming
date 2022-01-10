#!/usr/bin/python3
'''Show json using requests'''
import requests
from sys import argv


if __name__ == "__main__":
    try:
        q = argv[1]
    except Exception as e:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    data = r.json()
    if type(data) is dict and len(data) != 0:
        print('[{}] {}'.format(data.get('id'), data.get('name'))
    else:
        if len(data) == 0:
            print('No result')
        if type(data) is not dict:
            print('Not a valid JSON')
