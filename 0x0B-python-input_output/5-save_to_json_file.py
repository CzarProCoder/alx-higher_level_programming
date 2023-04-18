#!/usr/bin/python3

"""
Module to write an object onto a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (any type): Any type of py object
        filename (str): Name of a file to add string
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)
