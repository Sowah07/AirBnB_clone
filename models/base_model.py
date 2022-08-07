#!/usr/bin/python3
""" This Script contains the BaseModel class """


import uuid
from datetime import timezone
from datetime import time
from datetime import datetime
from datetime import timedelta


class BaseModel():
    """ Class BaseModel which is the superclass """

    def __init__(self, *args, **kwargs):
        """ Initialise an instance of BaseModel with id, created_at
        and updated_at """

        if kwargs != {}:
            created = kwargs['created_at']
            updated = kwargs['updated_at']
            kwargs['created_at'] = datetime.fromisoformat(created)
            kwargs['updated_at'] = datetime.fromisoformat(updated)
            for key, val in kwargs.items():
                if key != '__class__':
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Should print [<class name>] (self.id) <self.__dict__> """
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     str(self.id), str(self.__dict__)))

    def save(self):
        """ Updates the public instance attribute updated_at with
        current time """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary of all instance attributes """
        r = {}
        for key, val in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                r[key] = val.isoformat()
            else:
                r[key] = val
        r['__class__'] = self.__class__.__name__
        return r
