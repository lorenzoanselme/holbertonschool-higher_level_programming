#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for j in matrix[i]:
            if j == matrix[i][-1]:
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
        print("")
