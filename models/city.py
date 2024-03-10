#!/usr/bin/python3
"""
Defines City model and
inherits from BaseMode
"""


from models.base_model import BaseModel


class City(BaseModel):
    # City Model Class

    # Atributes in CityModel
    state_id: str = ''
    name: str = ''
