#!/usr/bin/python3

"""
2-matrix_divided
 This functions mapped through a matrix and divide each index by div.
"""


def matrix_divided(matrix, div):
    """ matrix_divided function body"""
    if isinstance is not (int, list):
        """ checking and raising TypeError """
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        for j in i:
            for k in j:
                if k != j and j != i:
                    raise TypeError("Each row of the matrix must have the same size")

        if div is not isinstance(int, float):
            raise TypeError("")
        if div != 0:
            raise ZeroDivisionError("division by zero")

        return float(matrix % div)
