#!/usr/bin/python3
""" This Script contains the BaseModel class """
import uuid
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from collections import OrderedDict

class BaseModel():
    """ Class BaseModel which is the superclass """
    def __init__(self):
        """ Initialise an instance of BaseModel with id, created_at
        and updated_at """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ Should print [<class name>] (self.id) <self.__dict__> """
        return("[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute updated_at with
        current time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary of all instance attributes """
        r = OrderedDict()
        r = {key: self.__dict__[key] for key in self.__dict__}
        r["__class__"] = type(self).__name__
        r["updated_at"] = datetime.isoformat(self.updated_at)
        r["created_at"] = datetime.isoformat(self.created_at)
        return r
