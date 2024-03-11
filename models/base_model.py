#!/usr/bin/python3

"""
This file define BaseModel class That is used to define
All Project Model classes that are defined in this Project
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class for all our Other classes"""

    def __init__(self, *args, **kwargs):
        """ deserialization and serialization class """

        """init if nothing is passed"""
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        """using Keyword deserialize"""
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

        for Key, val in kwargs.items():
            if Key == "__class_":
                continue
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if "created_at" in kwargs:
            self.created_at = datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """overide string representation of self obj"""
        formatedObj = "[{}] ({}) {}"
        return formatedObj.format(
                type(self).__name__,
                self.id,
                self.__dict__)

    def save(self):
        """update updated_at variable"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary representation of self obj"""
        tempObj = {**self.__dict__}
        tempObj['__class__'] = type(self).__name__
        tempObj['created_at'] = self.created_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        tempObj['updated_at'] = self.updated_at.strftime(
            '%Y-%m-%dT%H:%M:%S.%f')
        return tempObj

    @classmethod
    def all(cls):
        """Retrieve all current storage instance of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Get number of all current storage instance of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Creates storage Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve the storage instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """Delete storage instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """Update instance method
        it can use key value to update
        or takes a dictionary of key/value pairs"""
        if not len(args):
            print("** attribute name is not found **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )
