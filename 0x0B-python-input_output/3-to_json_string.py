#!/usr/bin/python3
"""
jsonto_string definition
"""
import json


def to_json_string(my_obj):
    """[summary]

    Args:
        my_obj ([type]): [description]

    Returns:
        [my_obj]: [json]
    """
    return json.dumps(my_obj)
