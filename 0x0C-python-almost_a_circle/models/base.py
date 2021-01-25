#!/usr/bin/python3
"""
class base definition
"""
import json
import os


class Base:
    """
    class base implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """

        Args:
            list_dictionaries ([dict]): [description]
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        for d in list_dictionaries:
            if type(d) != dict:
                raise TypeError("list_dictionaries must be a dictionary")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """[save json representation of objects]

        Args:
            list_objs ([type]): [description]
        """
        l_objects = []
        if not list_objs or list_objs is None:
            l_objects = []
        else:
            for obj in list_objs:
                l_objects.append(obj.to_dictionary())
        with open(cls.__name__ + '.json', 'w+', encoding='utf-8') as f:
            f.write(cls.to_json_string(l_objects))
        f.close()

    @staticmethod
    def from_json_string(json_string):
        """[returns the list of the JSON string]

        Args:
            json_string ([type]): [description]
        """
        if not json_string or json_string is None:
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """[summary]
        """
        if cls.__name__ == 'Square':
            new_instances = cls(1)
        elif cls.__name__ == 'Rectangle':
            new_instances = cls(1, 1)
        new_instances.update(**dictionary)
        return new_instances

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        file_name = cls.__name__ + '.json'
        new_list = []
        if not os.path.exists(file_name):
            return []
        with open(file_name, 'r', encoding='utf-8') as j_f:
            l_d = cls.from_json_string(j_f.read())
        for d in l_d:
            new_list.append(cls.create(**d))
        return new_list
