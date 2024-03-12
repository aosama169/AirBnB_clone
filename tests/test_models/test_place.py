#!/usr/bin/python3
"""Test Place class"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import pep8
import unittest


class Testplace(unittest.TestCase):
    """
    Unittest for Place class module
    """

    def test_pep8_conformance_place(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """
        Test if class is named correct
        """
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")

    def test_father(self):
        """
        Test if Class inherit from BaseModel
        """
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))
