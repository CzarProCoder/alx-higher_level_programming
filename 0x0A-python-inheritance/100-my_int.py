#!/usr/bin/python3

"""
Module containing MyInt that inherits from int
"""


class MyInt(int):
    """
    Class MyInt is a subclass of int
    """
    def __init__(self, num):
        """
        Initialize num
        """
        self.num = num

    def __eq__(self, other):
        """
        Method to invert == sign

        Return:
            False: if both are equal
            True: if both are not equal
        """
        return self.num != other

    def __ne__(self, other):
        """
        Methods to invert != sign

        Return:
            False: If both are not equal
            True: if both are equal
        """
        return self.num == other
