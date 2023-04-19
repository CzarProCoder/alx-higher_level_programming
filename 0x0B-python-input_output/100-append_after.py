#!/usr/bin/python3

"""
Module to insert a text after each line that contains a string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file,
    after each line containing a specific string
    """
    text = ""
    with open(filename, mode="r+", encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
        f.seek(0)
        f.write(text)
