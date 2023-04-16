#!/usr/bin/python3

"""
Module containing function to add a new attribute to an object
"""


def add_attribute(obj, att, value):
    """
    Function to add a new attribute to an object

    Raise a TypeError exception, with the message
    can't add new attribute if the object can’t have new attribute

    Args:
        obj (Instance): Instance of class to gain attribute
        att (attribute): Attribute to be added
        value (any type): Value to add to object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
