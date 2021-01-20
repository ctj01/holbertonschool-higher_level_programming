#!/usr/bin/python3
"""
add_atrribute definition
"""


def add_attribute(obj, name, value):
    """[summary]

    Args:
        obj ([type]): [description]
        name ([type]): [description]
        value ([type]): [description]

    Raises:
        TypeError: [description]
    """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
