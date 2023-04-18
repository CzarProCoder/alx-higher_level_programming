#!/usr/bin/python3

"""
Module to write text to a file
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file
    And returns the number of characters written

    Args:
        filename (str): Name of the file to be used
        text (str): Text to be written in the file

    Returns: The number of character written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
