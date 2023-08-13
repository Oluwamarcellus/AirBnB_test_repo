#!/usr/bin/env python3
"""
Test for FileStorage module
"""


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import datetime
import unittest
import models
from models.city import City


class TestStorage(unittest.TestCase):
    """
    Testing FileStorage class
    """

    def test_inst(self):
        """
        Testing instance type
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_storage_all(self):
        """
        Testing the all() method
        """
        storage = FileStorage()
        dic = storage.all()
        self.assertIsInstance(dic, dict)

    def test_new(self):
        """
        Testing the new() method
        """
        sample = City()
        models.storage.new(sample)
        self.assertIn("City." + sample.id, models.storage.all().keys())
        self.assertIn(sample, models.storage.all().values())

    def test_save(self):
        """
        Testing the save() method
        """
        sample = City()
        models.storage.new(sample)
        models.storage.save()
        with open("file.json", "r") as file:
            f_contents = file.read()
            self.assertIn("City." + sample.id, f_contents)

    def test_save_none(self):
        """
        Testing save with None as arg
        """
        with self.assertRaises(TypeError):
            models.storage.save(None)
