#!/usr/bin/python3

"""
Module to create a Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that defines a square
    Square is a subclass of Rectangle
    """
    def __init__(self, size):
        """
        Method initializing a Square of length 'size'

        Args:
            size (int): Length of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
