#!/usr/bin/python3

"""
Module that returns an object returns an object represented by json
"""

import json


def from_json_string(my_str):
    """
    Function to return object represented by json

    Args:
        my_str (str): string to be convert to py object

    Return:
        The object represented by json str
    """
    return(json.loads(my_str))
