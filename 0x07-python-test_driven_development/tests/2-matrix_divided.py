#!/usr/bin/python3
"""
    Module containing function to divide values in a matrix
"""


def matrix_divided(matrix, div):
    """
    Function to divide each value in a matrix
    containing list of lists of float or integer

    Args:
        matrix (list of lists): of floats  integer values
        div (integer or float): Values to be divided by div
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")

    matrix_len = len(matrix)
    matrix_index = 0

    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/floats")
    list_len = len(matrix[0])
    new_matrix = []

    for matrix_item in matrix:
        if not isinstance(matrix_item, list):
            raise TypeError("matrix must be a matrix \
                            (list of lists) of integers/floats")
        if len(matrix_item) != list_len:
            raise TypeError("Each row of the matrix must \
                            have the same size")

        item_index = 0
        new_list = []

        for value in matrix_item:
            if not isinstance(value, (float, int)):
                raise TypeError("matrix must be a matrix \
                                (list of lists) of integers/floats")
            new_value = value / div
            new_list.append(new_value)
            item_index += 1
        new_matrix.append(new_list)
        matrix_index += 1

    return new_matrix
