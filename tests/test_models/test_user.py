#!/usr/bin/python3
"""Test User class module"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import pep8
import unittest


class Testuser(unittest.TestCase):
    """
    Unittest for User class module
    """

    def test_pep8_conformance_user(self):
        """Test that we conform"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
