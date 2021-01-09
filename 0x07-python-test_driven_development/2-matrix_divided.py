#!/usr/bin/python3
""" module that divides all elements of a matrix of similar sized rows """


def matrix_divided(matrix, div):
    """ function that returns a new matrix with each element divided by da div
    Args:
        matrix: a 2d array, each row should be the same size or else: error
        div: a number that is not 0 or else error
    Returns: a new matrix with each element adjusted to the div amount
    """
    err = "matrix must be a matrix (list of lists) of integers/floats"
    new = []
    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(err)
    if type(div) is int or type(div) is float or div is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(err)
    for i in range(len(matrix)):
        if len(matrix[i]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        new.append([])
        for j in matrix[i]:
            if type(j) is int or type(j) is float:
                new[i].append(round(j / div, 2))
            else:
                raise TypeError(err)
    return new
