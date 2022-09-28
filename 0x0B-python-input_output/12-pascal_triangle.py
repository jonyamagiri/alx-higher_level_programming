#!/usr/bin/python3
"""
Module 12-pascal_triangle.py with method pascal_triangle.
"""


def pascal_triangle(n):
    """
    Accepts parameter n (an int).
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        pas_tri = triangles[-1]
        temp = [1]
        for i in range(len(pas_tri) - 1):
            temp.append(pas_tri[i] + pas_tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
