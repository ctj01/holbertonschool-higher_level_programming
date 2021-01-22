#!/usr/bin/python3
"""
class base definition
"""
import  sys
import  os
sys.path.insert(1, os.getcwd())

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