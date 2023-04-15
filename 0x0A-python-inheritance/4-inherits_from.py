#!/usr/python3

"""
Module to check if an an obj inherits from a class
"""


def inherits_from(obj, a_class):
    """
    Function to check whether an object inherits from a class

    Args:
        obj (Any type): Object to be checked
        a_class (class): Class to be evaluted against

    Returns:
        True: If an obj inherits directly or indirectly
        False: Does not inherit from the class in any way
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
