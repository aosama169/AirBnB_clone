#!/usr/bin/python3

"""
This file defines storage system for hbnb project
It will use JSON format for serialization and deserialization
"""

import json
from json.decoder import JSONDecodeError
from .errors import *
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class FileStorage:
    """
    This Class will serve Object mapping to file or database Storage
    """

    """class private varaibles used by this class"""
    __objects: dict = {}
    __file_path: str = 'file.json'
    models = (
            "BaseModel",
            "User", "City", "State", "Place",
            "Amenity", "Review"
            )

    def __init__(self):
        """constructor with no handle"""
        pass

    def all(self):
        """Return all instances stored in the file"""
        return FileStorage.__objects

    def new(self, obj):
        """Stores a new Object in the file"""
        keyObj = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[keyObj] = obj

    def save(self):
        """serializes objects stored in file"""
        serializedObj = {
            key: val.to_dict()
            for key, val in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(serializedObj))

    def reload(self):
        """deserialize persisted objects"""
        try:
            deserializedObj = {}
            with open(FileStorage.__file_path, "r") as f:
                deserializedObj = json.loads(f.read())
            FileStorage.__objects = {
                key:
                    eval(obj["__class__"])(**obj)
                    for key, obj in deserializedObj.items()}
        except (FileNotFoundError, JSONDecodeError):
            # If no file is found then do nothing.
            pass

    def find_by_id(self, model, obj_id):
        """Find and return an element of model by the id"""
        FS = FileStorage
        if model not in FS.models:
            # Invalid Model Name
            # Not yet Implemented
            raise ModelNotFoundError(model)

        keyObj = model + "." + obj_id
        if keyObj not in FS.__objects:
            # invalid id
            # Not yet Implemented
            raise InstanceNotFoundError(obj_id, model)

        return FS.__objects[keyObj]

    def delete_by_id(self, model, obj_id):
        """Find and return an elemt of model by its id"""
        FS = FileStorage
        if model not in FS.models:
            raise ModelNotFoundError(model)

        keyObj = model + "." + obj_id
        if keyObj not in FS.__objects:
            raise InstanceNotFoundError(obj_id, model)

        del FS.__objects[keyObj]
        self.save()

    def find_all(self, model=""):
        """Find all instances of model"""
        if model and model not in FileStorage.models:
            raise ModelNotFoundError(model)
        results = []
        for key, val in FileStorage.__objects.items():
            if key.startswith(model):
                results.append(str(val))
        return results

    def update_one(self, model, iid, field, value):
        """Updates an instance in the file"""
        FS = FileStorage
        if model not in FS.models:
            raise ModelNotFoundError(model)

        key = model + "." + iid
        if key not in FS.__objects:
            raise InstanceNotFoundError(iid, model)
        if field in ("id", "updated_at", "created_at"):
            # This is not allowed to be updated.
            return
        inst = FS.__objects[key]
        try:
            # if instance has that value cast it
            vtypeObj = type(inst.__dict__[field])
            inst.__dict__[field] = vtypeObj(value)
        except KeyError:
            # instance doesnot has the field.
            inst.__dict__[field] = value
        finally:
            inst.updated_at = datetime.utcnow()
            self.save()
