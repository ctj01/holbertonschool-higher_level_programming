#!/usr/bin/python3
"""
square class definition
"""
from models.rectangle import Rectangle


def check_values(atributte, value):
    """
    handling erros
    Args:
        atributte ([type]): [description]
        value ([type]): [description]

    Returns:
        [type]: [description]
    """
    atrr = {
        'width': int,
        'height': int
                    }

    if type(value) != int:
        raise TypeError("{} must be an integer".format(value))
    if (atributte in atrr) and value <= 0:
        raise ValueError("{} must be > 0".format(value))
    elif value < 0:
        raise ValueError("{} must be >= 0".format(value))


class Square(Rectangle):
    """

    Args:
        Rectangle ([type]): [description]
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def to_dictionary(self):
        x = {}
        a = self.__dict__
        s = ""
        if a:
            for key in a:
                s = key
                if key.startswith('_'):
                    s = key[12:]
                if s == 'width' or s == 'height':
                    s = "size"
                x[s] = a[key]
            return x

    def __str__(self):
        """
        str
        """
        return ('[Square] ({}) {}/{} - {}'.format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """
        overridinf update method
        """
        if args:
            atributtes = ['id', 'size', 'x', 'y']
            for key, value in enumerate(args):
                setattr(self, atributtes[key], value)
            return
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

    @property
    def size(self):
        """
        size getter
        Returns:
            [type]: [description]
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            size stter
        Args:
            value ([type]): [description]
        """
        check_values('width', value)
        self.width = value
        self.height = value
