#!/usr/bin/env python3
"""
Test for User module/class
"""


import unittest
from models.user import User
from models.base_model import BaseModel
import datetime

class UserTest(unittest.TestCase):
    """
    Test cases for user module
    """

    def test_str_repr(self):
        """
        Testing string representation
        """
        user = User()
        cls = user.__class__.__name__
        id_ = user.id
        strn = "[{}] ({}) {}".format(cls, id_, user.__dict__)
        self.assertEqual(user.__str__(), strn)

    def test_all_instances(self):
        """
        Testing instances
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_subclass(self):
        """
        Testing is User is a subclass of BaseModel
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_equals(self):
        """
        Testing for equalities
        """
        user = User()
        strn = ""
        self.assertEqual(user.email, strn)
        self.assertEqual(user.password, strn)
        self.assertEqual(user.last_name, strn)
        self.assertEqual(user.first_name, strn)
 
    def test_save(self):
        """
        Testing the save() influence on the updated_at attribute
        """
        user = User()
        old_save = user.updated_at
        user.save()
        new_save = user.updated_at
        self.assertNotEqual(old_save, new_save)
