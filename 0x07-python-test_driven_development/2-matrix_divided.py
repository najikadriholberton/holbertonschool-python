"""Matrix Divided Module"""


from typing import Type


def matrix_divided(matrix, div):
    """Matrix Divided Function"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif int(div) == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is list:
        row_size = len(matrix[0])
        for row in matrix:
            if type(row) != list:
                raise TypeError(
                    "matrix must be a matrix (list of lists)" +
                    " of integers/floats")
            if len(row) != row_size:
                raise TypeError(
                    "Each row of the matrix must have the same size")
        new_matrix = []
        for i in range(len(matrix)):
            new_matrix.append([])
            for j in range(row_size):
                val = matrix[i][j]
                if not isinstance(val, (int, float)):
                    raise TypeError(
                        "matrix must be a matrix (list of lists)\
                                of integers/floats")
                new_matrix[i].append(round(matrix[i][j]/div, 2))
        return new_matrix
    else:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
