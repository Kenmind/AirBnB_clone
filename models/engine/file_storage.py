#!/usr/bin/python3
"""
Defines a class that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes a class instance to a JSON file and
    deserializes a JSON file to an instance

    Private class attributes:
        @__file_path: string-path to the JSON file (ex: file.json)
        @__objects: dictionary-empty but will store objects by
        <class name>.id (ex: to store a BaseModel object with id=1212121212,
        the key will be BaseModel.1212121212)
    Public instance methods:
        @all(self): returns the dictionary __objects
        @new(self, obj): sets in __objects the obj with key
        <obj class name>.id
        @save(self): serializes __objects to the JSON file (path: __file_path)
        @reload(self): deserializes the JSON file to __objects (only
        if the JSON file (__file_path) exists; otherwise, do nothing. If
        the file doesn't exist, no exception should be raised)
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        Returns the dictionary of obj
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Appends new object to the var '__objects'

        Args:
                    @obj: object to append
        """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                                  obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file at __file_path
        """
        obj = {
                key: value.to_dict()
                for key, value in FileStorage.__objects.items()
                }
        with open(FileStorage.__file_path, "w") as J_File:
            json.dump(obj, J_File)

    def reload(self):
        """reload method deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    cls = obj_dict['__class__']
                    self.new(eval('{}({})'.format(cls, '**obj_dict')))
        except FileNotFoundError:
            pass
