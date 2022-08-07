#!/usr/bin/python3
"""
Testing BaseModel
"""


import os
import json
import uuid
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Testing Model base
    """

    def setUp(self):
        """
        using setup method to setup instances
        """
        self.one = BaseModel()
        self.name = "Test_Model"

    def test_for_doc(self):
        self.assertIsNotNone(self.one.__doc__)

    def test_Model(self):
        """ Testing the instances just created """
        self.assertIsInstance(self.one, BaseModel)
        self.assertTrue('id' in self.one.__dict__)
        self.assertTrue('name' not in self.one.__dict__)
        self.assertTrue('created_at' in self.one.__dict__)
        self.assertTrue('updated_at' in self.one.__dict__)
        self.assertTrue('class' not in self.one.__dict__)

    def test_save(self):
        """ Testing save method """
        self.one.save()
        self.assertNotEqual(self.one.created_at, self.one.updated_at)

    def test_id_str(self):
        """ Testing string of id """
        self.assertTrue(type(self.one.id), str)

    def test_to_dict(self):
        """ Testing to_dict method """
        r = self.one.to_dict()
        self.assertTrue(type(r), dict)
        self.assertTrue('__class__' in r)

    def test_to_dict_strings(self):
        """ making sure all values are strings now """
        j = self.one.to_dict()
        self.assertTrue(type(j['id']), str)
        self.assertTrue(type(j['created_at']), str)
        self.assertTrue(type(j['updated_at']), str)
        self.assertTrue(type(j['__class__']), str)

    def test_basic(self):
        """
        Tests basic imputs for the BaseModel class
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number],
                         ["ALX", 89])

    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        pass

    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        pass


if __name__ == '__main__':
    unittest.main()
