#!/usr/bin/python3
'''
Task: 2. Say my name
Test: ./tests/3-say_my_name.txt
Module: 3-say_my_name
'''


def say_my_name(first_name, last_name=""):
    '''
    Function to concat two strings
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
