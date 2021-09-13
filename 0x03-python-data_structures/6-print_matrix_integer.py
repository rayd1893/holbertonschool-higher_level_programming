#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            e = " "
            if j == len(matrix[0]) - 1:
                e = ""
            print("{:d}".format(matrix[i][j]), end=e)
        print("")
