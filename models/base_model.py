#!/usr/bin/python3
"""
This Script contains the BaseModel class
"""


from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Class BaseModel which is the superclass

    Attributes:
        id(str): Handles uuid
        created_at: assigns current datetime
        updated_at: updates current datetime

    Methods:
        __str__: prints the class name, id and creates a dictionary
        save(self): updates datetime
        to_dict(self): returns the dictionary values of the instance

    """

    def __init__(self):
        """ Initialise an instance of BaseModel with id, created_at
        and updated_at"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Should print [<class name>] (self.id) <self.__dict__> """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with
        current time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary of all instance attributes """
        r = {}
        for key, val in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                r[key] = val.isoformat()
            else:
                r[key] = val
        r["__class__"] = self.__class__.__name__
        return r
