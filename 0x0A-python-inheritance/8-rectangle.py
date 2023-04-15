#!/usr/bin/python3

"""
Module containing a class Rectangle.
Rectangle is a subclass of BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class defining a Rectangle which is a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle

        Args:
            width (int): Width of the rectangle
            height (int): Length of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
