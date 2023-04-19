#!/usr/bin/python3

"""
Module to return a list of integers representing
the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Function to return a list of integers representing
    Pascal of n

    Args:
        n (int): Number of lines

    Returns:
        Pascal triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        tri = triangle[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangle.append(tmp)
    return triangle
