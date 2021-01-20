#!/usr/bin/python3
"""
MyList class definition
"""


class MyList(list):
    """
    MyList implementation
    """
    def print_sorted(self):
        """
        print_sorted implementation
        """
        print(sorted(self))
