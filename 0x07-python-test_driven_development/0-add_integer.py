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
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
                return 89

    return int(a) + int(b)
