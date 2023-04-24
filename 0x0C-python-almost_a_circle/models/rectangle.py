#!/usr/bin/python3

"""
Module that defines Rectangle, a subclass of Base
"""
from models.base import Base

class Rectangle(Base):
    """
    class Rectangle, that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a class Rectangle 
        
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            x (int): X axis
            y (int): Y axis
            id (int): ID of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
