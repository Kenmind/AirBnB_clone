#!/usr/bin/python3
"""
Defines a class that will be the base for all the classes to be created in the AirBnB module.
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Base model where all classes inherit from
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel
        Args:
                    @args: arguments that have no key values
                    @kwargs: arguments with key and values
        """
        TIME = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, TIME)
                elif key == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
            else:
                models.storage.new(self)
