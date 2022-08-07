#!/usr/bin/python3
""" This Script contains the BaseModel class """


import uuid
from datetime import timezone
from datetime import time
from datetime import datetime
from datetime import timedelta
import models


class BaseModel():
    """ Class BaseModel which is the superclass """

    def __init__(self, *args, **kwargs):
        """ Initialise an instance of BaseModel with id, created_at
        and updated_at """

        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs != {}:
            for key, val in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                            val, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(val)
                else:
                    self.__dict__[key] = val
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __str__(self):
        """ Should print [<class name>] (self.id) <self.__dict__> """
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """ Updates the public instance attribute updated_at with
        current time """
        self.updated_at = datetime.utcnow()
        models.storage.save()

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
