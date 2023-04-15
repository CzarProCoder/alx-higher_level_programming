#!/usr/bin/python3

"""
Module containing a class BaseGeometry.
"""


class BaseGeometry():
    """
    Calculations class
    """
    def area(self):
        """
        No implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Function to validate a value
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        elif (value <= 0):
            raise ValueError("<name> must be greater than 0")
