#!/usr/bin/python3

"""
Script to add all arguments to a python list
"""
import os
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    file = "add_item.json"

    try:
        content = load_from_json_file(file)
    except FileNotFoundError:
        content = []
    save_to_json_file(content + argv[1:], file)
