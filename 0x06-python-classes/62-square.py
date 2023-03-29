#!/usr/bin/python3

""" Module to define a square of size 'size' """


class Square:
    """class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ class Square with a private attribute class

        Args:
             size (int): size of the new square
             position (tuple): tuple of 2 positive integers
        Functions:
            __init__(self, size, position)
            size(self)
            size(self, value)
            position(self)
            position(self, value)
            area(self)
            my_print(self)
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        private instance attribute getter

        Returns:
            position (tuple): must be a tuple of 2 positive integers,
            otherwise raise a TypeError exception with the message
            position must be a tuple of 2 positive integers
        """
        return (self.__position)

    def position(self, value):
        """
        private instance attribute setter

        Args:
            value (tuple): must be a tuple of 2 positive integers,
            otherwise raise a TypeError exception with the messag
            position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
