#!/usr/bin/python3
"""
def append_write_file(filename="", text=""):
"""


def append_write(filename="", text=""):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        text (str, optional): [description]. Defaults to "".
    """
    encoding = "utf-8"
    with open(filename, "a", encoding=encoding) as file:
        file.write(text)
        file.close()
        return len(text)
