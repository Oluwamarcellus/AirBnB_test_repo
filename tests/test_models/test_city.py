#!/usr/bin/env python3
"""
Test for City class
"""


import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test cases for City module
    """

    def test_str_repr(self):
        """
        Testing string representation
        """
        city = City()
        cls = city.__class__.__name__
        id_ = city.id
        strn = "[{}] ({}) {}".format(cls, id_, city.__dict__)
        self.assertEqual(city.__str__(), strn)

    def test_all_instances(self):
        """
        Testing instances
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_subclass(self):
        """
        Testing if City is a subclass of BaseModel
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_equals(self):
        """
        Testing for equalities
        """
        city = City()
        strn = ""
        self.assertEqual(city.name, strn)
        self.assertEqual(city.state_id, strn)
 
    def test_save(self):
        """
        Testing the save() influence on the updated_at attribute
        """
        city = City()
        old_save = city.updated_at
        city.save()
        new_save = city.updated_at
        self.assertNotEqual(old_save, new_save)
