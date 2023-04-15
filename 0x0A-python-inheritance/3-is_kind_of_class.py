#!/usr/bin/python3

"""
Module to check if an obj is a kind of instance to a class
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if an object is an instance of,
    or if the object is an instance of a class

    Args:
        obj (Any type): Object to be checked
        a_class (class): Class to be evaluated

    Returns:
        True: If object is an instance
        False: If an object is not an instance
    """
    return isinstance(obj, a_class)
