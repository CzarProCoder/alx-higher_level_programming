#!/usr/bin/python3

"""
Script to add all arguments to a python list
"""
import sys
import os.path


if __name__ == "__main__":
    save_file = __import__('5-save_to_json_file').save_to_json_file
    load_file = \
        __import__('6-load_from_json_file').load_from_json_file

    my_list = []
    if os.path.exists("add_item.json"):
        my_list = load_file("add_item.json")

    for arg in sys.argv[1:]:
        my_list.append(arg)
    save_file(my_list, "add_item.json")
