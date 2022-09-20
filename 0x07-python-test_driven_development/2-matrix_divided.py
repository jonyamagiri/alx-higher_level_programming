#!/usr/bin/python3
"""
Module 2-matrix_divided.py, with method matrix_divided(matrix, div).
Divides all elements of a matrix and returns new matrix.
"""


def matrix_divided(matrix, div):
    """
    Accepts a matrix that is a list (lists of integers or floats),
    and a div that must be a number (integer or float).
    All elements of matrix are divided by div, rounded to 2 decimal places
    Returns a new matrix (the result).
    """
    new_matrix = []
    msg_1 = "Each row of the matrix must have the same size"
    msg_2 = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError(msg_1)
        second_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError(msg_2)
            else:
                second_list.append(round(items / div, 2))
        new_matrix.append(second_list)

    return new_matrix
