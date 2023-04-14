#!/usr/bin/python3

"""
Module to check attributes and methods of an object
"""


def lookup(obj):
    """
    Function to return the available attributes and methods of an object

    Args:
        obj (Any): Object to be checked

    Return:
        Attributes and methods of obj
    """

    return(dir(obj))
