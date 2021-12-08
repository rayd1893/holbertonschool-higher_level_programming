#!/usr/bin/python3


def remove_char_at(str, n):
    str2 = ""
    strlen = len(str)
    if n < 0 or n >= strlen:
        str2 = str
    elif n == 0:
        str2 = str[1:]
    else:
        str2 = str[:n] + str[n+1:]

    return str2
