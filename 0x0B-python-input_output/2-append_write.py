#!/usr/bin/python3

"""
Module to append text to a file
"""


def append_write(filename="", text=""):
    """
    Function to append text to a file

    Args:
        filename (str): Name of the file
        text (str): Text to be added to a file

    Returns:
        n (int): Number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return(f.write(text))
