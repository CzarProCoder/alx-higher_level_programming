#!/usr/bin/python3
"""
Module to define a rectangle class
"""


class Rectangle:
    """
    Class defining a rectangle

    Attributes
        number_of_instances (int): Initializes to zero
        Increments by 1 when a rectange instance is created
        Decrements by 1 when a rectange is destroyed

        print_symbol (any): Used as symbol for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Method to initialize the rectange

        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectange
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """
        Method to calculate the area of rectangle

        Returns:
            height x width (int): area of rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Method to calculate the perimeter of the rectangle


        Returns:
            (width + height)*2 (int): Perimeter of the rectange
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """
        Method defining how the rectange if printed using print or str
        functions

        Returns:
            rect (string): String made of #
        """
        rect = ""
        if self.__height == 0 or self.__width == 0:
            return (rect)
        for i in range(self.__height):
            rect += (str(self.print_symbol) * self.__width) + "\n"
        return rect[:-1]

    def __repr__(self):
        """ This method returns the string represantion of the rectange
        Returns:
            string represenation of the rectangle
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        Method to detect the deletion of a rectange
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2