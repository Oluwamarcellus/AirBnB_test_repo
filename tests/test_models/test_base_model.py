#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the base_model
    """
    def test_str(self):
        """Check string output from BaseModel"""
        base = BaseModel()
        self.asserEqual(base.__str__(), f"[{type(base).__name__}] ({base.id}] {base.__dict__}")


    def test_save(self):
        """Test save method"""
        base = BaseModel()
        base_time = base.updated_at
        base.save()
        newtime = base.updated_at
        self.assertEqual(base_time, newtime)
        
    def test_to_dict(self):
        """
        Test to_daict() function from basemodel
        """
        base = BaseModel()
        prev_time = base.updated_at
        self.assertDictEqual(base.to_dict(),
                             {'__class__': type(base).__name__,
                              'updated_at': base.updated_at.isoformat(),
                              'id': base.id,
                              'created_at': base.created_at.isoformat()})
        base.save()
        self.assertNotEqual(prev_time, base.updated_at)

    def test_attr_classes(self):
        """
        checks if the right classes were use to generate attributes
        """
        base = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertNotEqual(base.id, base2.id)
