#!/usr/bin/python3
"""
This file inherting BaseModel defining UserModel class
"""

from models.base_model import BaseModel


class User(BaseModel):
    # User Model Class

    # class attributes in UserModel
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
