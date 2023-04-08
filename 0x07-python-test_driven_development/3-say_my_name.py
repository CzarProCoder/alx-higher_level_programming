#!/usr/bin/python3
"""
Module for function to print names
"""


def say_my_name(first_name, last_name=""):
    """
    Function to calculate print the first and last_name

    Args:
        first_name: First name to be printed
        last_name: Last_name to be printed
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
