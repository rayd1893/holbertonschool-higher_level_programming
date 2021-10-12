#!/usr/bin/python3
'''Load file json'''


import json


def load_from_json_file(filename):
    '''Define function'''
    with open(filename) as f:
        return json.loads(f.read())
