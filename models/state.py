#!/usr/bin/python3
"""
This file define stateModel class inherting BaseModel
"""


from models.base_model import BaseModel


class State(BaseModel):
    # state model Class

    # Atrributes in state model
    name: str = ''
