#!/usr/bin/python3
def multiple_returns(sentence):
    len_string = len(sentence)
    first = None

    if sentence != "":
        first = sentence[0]
    return len_string, first
