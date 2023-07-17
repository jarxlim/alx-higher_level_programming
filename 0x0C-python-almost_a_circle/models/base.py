#!/usr/bin/python3
"""Documentation for Base class"""


import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation function for Base instanc"""

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list_objects = []
        if list_objs is not None:
            for i in list_objs:
                list_objects.append(cls.to_dictionary(i))
        with open(filename, 'w', encoding='utf-8') as myFile:
            myFile.write(cls.to_json_string(list_objects))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new_base = cls(1, 1)
        elif cls.__name__ == "Square":
            new_base = cls(1)
        new_base.update(**dictionary)
        return new_base

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file with JSON object"""
        filename = cls.__name__ + ".json"
        newlist = []
        try:
            with open(filename, 'r', encoding='utf-8') as myFile:
                newlist = cls.from_json_string(myFile.read())
            for i, e in enumerate(newlist):
                newlist[i] = cls.create(**newlist[i])
        except:
            pass
        return newlist
