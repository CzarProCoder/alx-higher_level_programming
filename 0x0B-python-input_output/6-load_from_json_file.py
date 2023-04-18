#!/usr/bin/python3

"""
Module to create an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    Function to create an object from a json file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        text = f.read()
    return(json.loads(text))
