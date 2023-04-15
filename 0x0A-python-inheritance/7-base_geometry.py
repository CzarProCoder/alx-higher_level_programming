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
            raise TypeError("{:s} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError(f"{:s} must be greater than 0".format(name))
