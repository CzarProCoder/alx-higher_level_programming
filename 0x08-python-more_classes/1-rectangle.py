#!/usr/bin/python3
"""
Module to define a rectangle class
"""


class Rectangle:
    """
    Class defining a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Method to initialize the rectange

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectange
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter/Setter to return the width of the rectange

        Returns:
            Returns the width of the rectange
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Method to set the width

        Args:
            value (int): Value to set as width

        Raises:
            TypeError: If the value if not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter/Setter to return the height of the rectange

        Returns:
            Returns the height of the rectange
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Method to set the height

        Args:
            value (int): Value to set as height

        Raises:
            TypeError: If the value if not an integer
            ValueError: If the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
