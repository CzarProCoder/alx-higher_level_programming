#!/usr/bin/python3

"""
Module to define class Base
"""


class Base():
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instance of the class

        Args:
            id: Takes in id as the only argument for initialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
