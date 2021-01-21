#!/usr/bin/python3
"""
def write_file(filename="", text=""):
"""


def write_file(filename="", text=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    encoding = "utf-8"
    with open(filename, "w", encoding=encoding) as file:
        file.write(text)
        file.close()
        return len(text)
