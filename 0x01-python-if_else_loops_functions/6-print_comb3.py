#!/usr/bin/python3
for i in range(0, 10):
    for j in range(0, 10):
        if i < j and i != 8 and i != 9:
            print("{}{}".format(i, j), end=', ')
print("{}".format(89))
