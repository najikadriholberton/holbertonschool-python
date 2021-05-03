#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            space = "" if j == m-1 else " "
            print("{:d}".format(matrix[i][j]), end=space)
        print()
