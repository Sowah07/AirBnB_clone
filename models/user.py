#!/usr/bin/python3
""" State class """
from .base_model import BaseModel


class User(BaseModel):
    """Creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
