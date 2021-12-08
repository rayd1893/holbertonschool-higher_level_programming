#!/usr/bin/python3


def uppercase(str):
    n = len(str)
    str2 = ""
    for i in range(0, n):
        o = ord(str[i])
        if o >= 97 and o <= 122:
            str2 += chr(o - 32)
        else:
            str2 += chr(o)
    print("{}".format(str2))
