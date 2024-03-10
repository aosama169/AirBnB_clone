#!/usr/bin/python3
"""
Define errors in file storage Module
"""


class ModelNotFoundError(Exception):
    """Is raised when unknown module is passed"""
    def __init__(self, arg="BaseModel"):
        super().__init__(f"Model with name {arg} is not found!")


class InstanceNotFoundError(Exception):
    """Is raised when unknown id is passed"""

    def __init__(self, obj_id="", mod="BaseModel"):
        super().__init__(
                f"Instance of {mod} with id {obj_id} not exists!")
