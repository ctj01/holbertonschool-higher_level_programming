#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = []
    for f in matrix:
        x.append(list(map(lambda a: a ** 2, f)))
    return x
