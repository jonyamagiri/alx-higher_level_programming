#!/usr/bin/python3
"""
Module 2-matrix_divided.py, with method matrix_divided(matrix, div).
Divides all elements of a matrix and returns new matrix.
"""


def matrix_divided(matrix, div):
    """
    Adds 2 integers (a and b) that are integers or floats.
    a and b first casted to integers if they are float.
    Returns an integer: the addition of a and b.
    """
    new_matrix = []
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        second_list = []
        for items in lists:
            if not isinstance(items, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                second_list.append(round(items / div, 2))
        new_matrix.append(second_list)
        
    return new_matrix
