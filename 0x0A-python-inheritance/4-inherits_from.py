#!/usr/bin/python3
"""
is inherit from definition
"""


def inherits_from(obj, a_class):
    """
    is inherit from definition
    """
    return issubclass(obj.__class__, a_class) and type(obj) != a_class
