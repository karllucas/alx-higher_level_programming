#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    transposed = []
    for i in range(3):
        transposed.append([row[i] for row in matrix])
    print('{}'.format(transposed))
