#!/usr/bin/python3
"""Test Review class module"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import pep8
import unittest


class Testreview(unittest.TestCase):
    """
    Unittests for the Review class module
    """
    def test_pep8_conformance_review(self):
        """Test that we conform"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class(self):
        """
        Test if class is named correctly
        """
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_father(self):
        """
        Test if Class inherit from BaseModel
        """
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))
