#!/usr/bin/python3
'''Show json using requests'''
import requests
from sys import argv


if __name__ == "__main__":
    q = ""
    if len(argv) == 2:
        q = argv[1]
    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
        data = r.json()
        if data:
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except Exception as e:
        print('Not a valid JSON')
