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

    def area(self):
        """
        Method to calculate the area of rectangle

        Args:
            width (int): Width of the rectangle
            length (int): Length of the rectangle

        Returns:
            Areas of rectangle (width * length)
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Method to format the structure of print and format
        """
        return(f"[Rectangle] {self.__width}/{self.__height}")
