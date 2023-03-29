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

    @property
    def size(self):
        """
        property setter

        Returns:
            size (int): Returns the private attribute size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        property setter

        Args:
            size (int): Only parameter is size which is a private attribute
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Instance method to find area of Square
        Returns:
            area (int): area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        prints a square
        """
        counter = 0
        if self.__size == 0:
            print()
        else:
            while counter < self.__size:
                counter2 = 0
                while counter2 < self.__size:
                    print("#", end="")
                    counter2 += 1
                print()
                counter += 1
