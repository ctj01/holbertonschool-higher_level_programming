#!/usr/bin/python3
"""
is a BaseGeometry class definition
"""


class BaseGeometry:
    """
    BaseGeometry class implementation
    """
    pass

    def area(self):
        """[summary]

        Raises:
            Exception: area no implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """[summary]

        Args:
            name ([str]): [description]
            value ([int]): [description]

        Raises:
            TypeError: [if values is not integer]
            ValueError: [if value in less than 0]
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
