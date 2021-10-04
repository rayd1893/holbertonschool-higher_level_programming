#!/usr/bin/python3
'''
Task: 1. Divide a matrix
Test: tests/2-matrix_divided.txt
Module: 2-matrix_divided
'''


def matrix_divided(matrix, div):
    '''
    Divide matrix(List of lists)
    '''
    new_matrix = []
    new_list = []
    message1 = "matrix must be a matrix (list of lists) of integers/floats"
    message2 = "Each row of the matrix must have the same size"
    if not any(isinstance(el, list) for el in matrix):
        raise TypeError(message1)

    for i in range(len(matrix)):
        for j in matrix[i]:
            if type(j) not in [int, float]:
                raise TypeError(message1)
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError(message2)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_list = []
        for ele in row:
            new_list.append(round(ele / div, 2))
        new_matrix.append(new_list)
    return new_matrix
