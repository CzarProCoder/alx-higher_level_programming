#!/usr/bin/python3

"""
Module to print a list in ascending order
"""


class MyList(list):
    """
    "MyList" is a child/derived class of parent/base class "list"
    """

    def print_sorted(self):
        """
        Public instance that prints the list
        but sorted in ascending order
        """
        print(sorted(self))
