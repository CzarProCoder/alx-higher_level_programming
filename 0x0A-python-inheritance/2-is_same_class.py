#!/usr/bin/python3

"""
Module to check the if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Function to check when an obj is an instance of
    a_class

    Examples:
        >>> is_same_class = __import__('2-is_same_class').is_same_class
        >>> a = 20
        >>> is_same_class(20, int)
        True

        >>> name = 'Hello'
        >>> is_same_class(name, int)
        False

        >>> name = "Mwaura"
        >>> is_same_class(name, int)
        False
        >>> is_same_class(name, str)
        True

    Args:
        obj (Any type): Object to be checked
        a_class (any_type): Class to be used

    Return:
        True if obj is an instance of 'a_class'
        False if otherwise
    """
    return type(obj) == a_class
