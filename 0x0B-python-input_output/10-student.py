#!/usr/bin/python3

"""
Module containing the class Student
"""


class Student:
    """
    Class defining the attributes of student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes the class objects
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dict representation of Student intance
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic
