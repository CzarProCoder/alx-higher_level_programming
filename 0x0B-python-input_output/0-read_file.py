#!/usr/bin/python3

"""
Module to read and print contents of a file
"""


def read_file(filename=""):
    """
    Function to open, read and display the contents of a file

    Args:
        filename (str): Name of the file to be used
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
