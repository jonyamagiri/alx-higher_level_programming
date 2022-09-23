#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul.py, with method lazy_matrix_mul(m_a, m_b).
Defines a function that multiplies 2 matrices by using the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Accepts two matrices (m_a and m_b).
    Arguments:
        m_a (list of lists of ints or floats): 1st matrix
        m_b (list of lists of ints or floats): 2nd matrix
    Returns a new matrix which is a product of the two matrices.
    """
    return numpy.dot(m_a, m_b)
