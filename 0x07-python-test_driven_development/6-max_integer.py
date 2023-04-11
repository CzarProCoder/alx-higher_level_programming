#!/usr/bin/python3
"""
    Module to check the Largest number from a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None

        Args:
            list (list): List containing integers
    """
    if len(list) == 0:
        return None
    Largest = list[0]
    i = 1
    while i < len(list):
        if list[i] > largest:
            largest = list[i]
        i += 1
    return largest
