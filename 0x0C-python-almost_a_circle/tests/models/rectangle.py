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
        """Initializes a class Rectangle

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

    @property
    def height(self):
        """ Get the width of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the width of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get the width of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the width of the rectangle """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get the width of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the width of the rectangle """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Method to calculate the area of a rectangle """
        return (self.width * self.height)

    def display(self):
        """Prints to stdout the rectangle instance"""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """Modifies the inbuilt method init"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.__x, self.__y,
            self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Update method

        Args:
            1st Item (int): Item at Index 0 is assigned to the id
            2nd Item (int): Index 1 -> To width
            3rd Item (int): Index 2 -> To height
            4th Item (int): Index 3 -> To x
            5th Item (int): Index 4 -> To y
        """
        if args is not None and len(args) > 0:
            for key, value in enumerate(args):
                if key == 0:
                    self.id = value
                elif key == 1:
                    self.width = value
                elif key == 2:
                    self.height = value
                elif key == 3:
                    self.x = value
                elif key == 4:
                    self.y = value
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
