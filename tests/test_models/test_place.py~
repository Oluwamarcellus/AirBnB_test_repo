#!/usr/bin/python3
"""
TEST
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestBaseModel(unittest.TestCase):
    def test_str(self):
        """Test str methog in place"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_p(self):
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))
