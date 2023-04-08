#!/usr/bin/python3
"""
Module to print a square of size using #
"""


def print_square(size):
    """
    Function to print a square

    Args:
        size (int): Size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
