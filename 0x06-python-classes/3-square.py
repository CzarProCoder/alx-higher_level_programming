#!/usr/bin/python3

""" Module to define a square of size 'size' """


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """ class Square with a private attribute class

        Args:
             size (int): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Instance method to find area of Square
        Return:
            area (int): area of the square
        """
        self.area = self.__size ** 2
        return (self.area)
