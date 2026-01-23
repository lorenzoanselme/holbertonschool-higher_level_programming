#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    idx = 0
    for i in range(0, len(matrix)):
        for j in matrix[i]:
            result = j ** 2
            new_matrix[i][idx] = result
            idx += 1
            if idx == len(matrix[i]):
                idx = 0
    return new_matrix
