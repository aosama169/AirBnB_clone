#!/usr/bin/env python3
""" unittest for base model class and method"""


import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from uuid import uuid4


class TestBaseModel(unittest.TestCase):
    """ define unittest for base model """

    def setUp(self):
        """ setup for ongoing tests """
        self.model = BaseModel()
        self.model.name = "My Base Model"
        self.model.my_number = 95

    def test_id_type(self):
        """ test for id variable type """
        self.assertEqual(type(self.model.id), str)

    def test_name_type(self):
        """ test for name variable type """
        self.assertEqual(type(self.model.name), str)

    def test_my_number_type(self):
        """ test for my number variable type """
        self.assertEqual(type(self.model.my_number), int)

    def test_created_at_type(self):
        """ test for created at variable type """
        self.assertEqual(type(self.model.created_at), datetime)

    def test_updated_at_type(self):
        """ test for updated at variable type """
        self.assertEqual(type(self.model.updated_at), datetime)

    def test_save_updates_updated_at(self):
        """ test for save updated at variable """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_contains_correct_keys(self):
        """ test for dictionary containing correct keys """
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_returns_dict(self):
        """ test for to dictionary return variable type """
        self.assertEqual(type(self.model.to_dict()), dict)

    def test_to_dict_created_at_format(self):
        """ testing for created at format found """
        model_dict = self.model.to_dict()
        created_at = model_dict['created_at']
        self.assertEqual(created_at, self.model.created_at.isoformat())

    def test_to_dict_updated_at_format(self):
        """ testing for updated at format """
        model_dict = self.model.to_dict()
        updated_at = model_dict['updated_at']
        self.assertEqual(updated_at, self.model.updated_at.isoformat())


class TestBaseModelTwo(unittest.TestCase):
    """ define unittests for base model two """

    def setUp(self):
        """ setup for proceeding tests two """
        self.my_model = BaseModel()

    def test_id_generation(self):
        """ test for id generation type """
        self.assertIsInstance(self.my_model.id, str)

    def test_to_dict_method(self):
        """ test for to dictionary method """
        my_model_dict = self.my_model.to_dict()
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

    def test_str_representation(self):
        """ test for str rrepresentation """
        expected = "[BaseModel] ({}) {}".format(
            self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected)

    def test_from_dict_method(self):
        """ test for dictionary methods """
        my_model_dict = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_dict)
        self.assertIsInstance(my_new_model, BaseModel)
        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.created_at, self.my_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.my_model.updated_at)

    def test_created_at_and_updated_at_types(self):
        """ test for created at and updated at var types """
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)


class TestBaseModelThree(unittest.TestCase):
    """ define unittests for base model three """

    def test_state(self):
        """ test for state object class """
        state = State()
        state.name = "Egypt"
        self.assertEqual(state.name, "Egypt")

    def test_amenity(self):
        """ test for amenity object class """
        amenity = Amenity()
        amenity.name = "Sea View"
        self.assertEqual(amenity.name, "Sea View")

    def test_city(self):
        """ test for city object class """
        state_id = uuid4()
        city = City()
        city.name = "Cairo"
        city.state_id = state_id
        self.assertEqual(city.name, "Cairo")
        self.assertEqual(city.state_id, state_id)

    def test_review(self):
        """ testing review object class"""
        place_id = uuid4()
        user_id = uuid4()
        review = Review()
        review.place_id = place_id
        review.user_id = user_id
        review.text = "Great"
        self.assertEqual(review.place_id, place_id)
        self.assertEqual(review.user_id, user_id)
        self.assertEqual(review.text, "Great")


if __name__ == "__main__":
    unittest.main()
