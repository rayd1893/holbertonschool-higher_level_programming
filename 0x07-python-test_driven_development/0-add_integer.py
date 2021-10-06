#!/usr/bin/python3
"""
Task: 0. Integers addition
Test: ./tests/0-add_integer.txt
Module: 0-add_integer
"""


def add_integer(a, b=98):
    """
    Function add_integer: Add two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)