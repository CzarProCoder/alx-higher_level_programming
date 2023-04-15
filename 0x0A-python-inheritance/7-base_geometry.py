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

        Args:
            name (string): String to be used
            value (int): Integer to be evaluated
        """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        elif (value <= 0):
            raise ValueError("<name> must be greater than 0")
