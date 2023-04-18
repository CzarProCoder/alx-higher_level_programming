#!/usr/bin/python3

"""
Module ro return json representation of a string
"""

import json


def to_json_string(my_obj):
    """
    Function to return json representation of an obj
    """
    return(json.dumps(my_obj))
