#!/usr/bin/env python3


from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import datetime
import unittest
import models
from models.city import City


class TestStorage(unittest.TestCase):

    def test_inst(self):
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_storage_all(self):
        storage = FileStorage()
        dic = storage.all()
        self.assertIsInstance(dic, dict)

    def test_new(self):
        sample = City()
        models.storage.new(sample)
        self.assertIn("City." + sample.id, models.storage.all().keys())
        self.assertIn(sample, models.storage.all().values())

    def test_save(self):
        sample = City()
        models.storage.new(sample)
        models.storage.save()
        with open("file.json", "r") as file:
            f_contents = file.read()
            self.assertIn("City." + sample.id, f_contents)

    def test_save_none(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)
