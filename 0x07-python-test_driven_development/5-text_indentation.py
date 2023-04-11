#!/usr/bin/python3
"""
Module to print a text with 2 new lines after each
of these characters .?:
"""


def text_indentation(text):
    """
    Function to print a text with 2 linesi

    Args:
        text(string): Takes some text as only parameter

    Returns:
        new-text (string): Returns new text with .?: being replaced by space
    """
    if not isinstance(text, string):
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    list_lines = [lines.strip(' ') for lines in text.split('\n')]
    new_text = "\n".join(list_lines)
    print(new_text, end="")
