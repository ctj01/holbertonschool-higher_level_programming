#!/usr/bin/python3
"""
MyList class definition
"""


class MyList(list):
    """
    MyList implementation
    """
    def print_sorted(self):
        print(sorted(self))
