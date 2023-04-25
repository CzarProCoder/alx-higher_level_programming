#!/usr/bin/python3

"""
Module to define the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square inherits from Rectangle
    Rectangle is a class in the models module
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Modifies the inbuilt method init"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.width)
