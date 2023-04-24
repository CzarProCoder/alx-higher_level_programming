#!/usr/bin/python3

import unittest
import os
from models.base import Base
# from models.square import Square
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """Test suite for base class"""
    def setup(self):
        """Method to set initial number of objects"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Creating an instance of Base clas"""
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """Method to test default id"""
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """Testiing number of objects"""
        new1 = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new1.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """Test the number of object attributes and assigned id"""
        new1 = Base()
        new2 = Base(1523)
        new3= Base()
        self.assertEqual(new1.id, 1)
        self.assertEqual(new2.id, 1523)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ Test string id"""
        new = Base('2')
        self.assertEqual(new.id, '2')

    def test_more_ids(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attr(self):
        """Testing the private attributes"""
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects


if __name__ == "__main__":
    unittest.main()
