#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = len(matrix)
    m = len(matrix)
    mat = []
    for i in range(n):
        mat.append([])
        for j in range(m):
            mat[i].append(matrix[i][j] ** 2)
    return mat
