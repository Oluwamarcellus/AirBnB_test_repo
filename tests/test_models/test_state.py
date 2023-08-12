#!/usr/bin/env python3
"""
Test for State class
"""


import unittest
from models.state import State
from models.base_model import BaseModel
import datetime


class TestState(unittest.TestCase):
    """
    Test cases for State module
    """

    def test_str_repr(self):
        """
        Testing string representation
        """
        state = State()
        cls = state.__class__.__name__
        id_ = state.id
        strn = "[{}] ({}) {}".format(cls, id_, state.__dict__)
        self.assertEqual(state.__str__(), strn)

    def test_all_instances(self):
        """
        Testing instances
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_subclass(self):
        """
        Testing if State is a subclass of BaseModel
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_equals(self):
        """
        Testing for equalities
        """
        state = State()
        strn = ""
        self.assertEqual(state.name, strn)

    def test_save(self):
        """
        Testing the save() influence on the updated_at attribute
        """
        state = State()
        old_save = state.updated_at
        state.save()
        new_save = state.updated_at
        self.assertNotEqual(old_save, new_save)
