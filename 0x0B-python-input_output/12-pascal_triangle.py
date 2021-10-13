#!/usr/bin/python3
'''Trinagle of Pascal'''


def pascal_triangle(n):
    '''Define function'''
    my_list = []

    if n >= 1:
        my_list.append([1])

    if n >= 2:
        my_list.append([1, 1])

    for i in range(3, n + 1):
        sub = []
        sub.append(1)
        for j in range(1, i - 1):
            other_list = (my_list[i - 2])
            sub.append(other_list[j - 1] + other_list[j])
        sub.append(1)
        my_list.append(sub)

    return my_list
