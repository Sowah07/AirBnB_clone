#!/usr/bin/python3
""" Filestorage that serializes instances to a json file
and deserializes json file to instances """


import json


class FileStorage():
    """ Serialize and deserialize instances """

    __file_path = "data.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in objects the obj with key <obj c_name>.id """
        FileStorage.__objects[obj.__class__.__name__ + '.' + str(obj.id)] = obj

    def save(self):
        """ serializes __objects to json file path """
        dicts = {}
        for key, vals in FileStorage.__objects.items():
            dicts[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dicts, f, indent=4)

    def reload(self):
        """ deserializes the json file """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                dicts = json.load(f)
                for val in dicts.values():
                    cls = val["__class__"]
                    self.new(eval(cls)(**val))
        except Exception:
            pass
