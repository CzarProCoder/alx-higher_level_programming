#!/usr/bin/python3

"""
Returns the  dictionary description with simple
data structure
"""


def class_to_json(obj):
    """
    Function to return dictionary description with
    simple data structure

    Args:
        obj(Any Type): Object to be checked
    """
    return(obj.__dict__)
