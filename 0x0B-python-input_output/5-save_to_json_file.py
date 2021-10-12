#!/usr/bin/python3
'''Write file joson'''


import json


def save_to_json_file(my_obj, filename):
    '''Define function'''
    with open(filename, mode="w") as f:
        f.write(json.dumps(my_obj))
