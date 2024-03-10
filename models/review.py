#!/usr/bin/python3
"""
Define review model and inheriting BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    # Review model Class

    # Attributes in Review Model
    place_id: str = ''
    user_id: str = ''
    text: str = ''
