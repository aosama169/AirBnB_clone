#!/usr/bin/python3
"""
Defines  the Amenity model inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    # Amenity Mode Class

    # Attributes in the class
    name: str = ''
