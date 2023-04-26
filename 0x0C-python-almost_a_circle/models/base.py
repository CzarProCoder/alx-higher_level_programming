#!/usr/bin/python3

"""
Module to define class Base
"""
import json


class Base():
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instance of the class

        Args:
            id: Takes in id as the only argument for initialization
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method to return the json represention of list_dictionaries

        Args:
            list_dictionaries (dictionary): Dictionary to be checked
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
