#!/usr/bin/python3
"""A function that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """Matrix division module
    
    @matrix: matrix to be divided composed of ints or floats
    @div: int to be used to divide
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    n_mat = matrix.copy()
    if div == 0;
    raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
