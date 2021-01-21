#!/usr/bin/python3
"""
def read_file definition
"""


def read_file(filename=""):
    """

    Args:
        filename (str, optional): [name of file to read]. Defaults to "".
    """
    encoding = "utf-8"
    with open(filename, "r", encoding=encoding) as file:
        print(file.readlines())
        file.close()
