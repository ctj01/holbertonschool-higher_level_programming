#!/usr/bin/python3
"""
save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """[summary]

    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
        f.close()
