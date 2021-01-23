#!/usr/bin/python3
"""
rectangle class definition
"""

from models.base import Base


def check_values(atributte, value):
    x = {'height' : int,
        'width' : int,
        }
    if type(value) != int:
        raise  TypeError("{} must be an integer".format(value))
    if (atributte in x) and value <= 0:
        raise ValueError("{} must be > 0".format(value))
    elif  value < 0:
        raise ValueError("{} must be >= 0".format(value))

class Rectangle(Base):
    """

    Args:
        Base ([type]): [description]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the attributtes."""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """return the area of the rectangule."""
        return self.__width * self.__height

    def display(self):
        """draw the rectangle"""
        iterator = False
        if self.area() == 0:
            print('')
            return
        if self.__y > 0:
            print('\n' * (self.__y - 1))
        for x in range(self.__height):
            if iterator:
                print()
            if self.__x > 0:
                print(' ' * self.__x, end='')
            for item in range(self.__width):
                iterator = True
                print("#", end='')
        print()

    def __str__(self):
        """
        overrindin str mthod
        """
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        """getter width."""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width."""
        check_values('width', value)
        self.__width = value

    @property
    def height(self):
        """getter height."""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height."""
        check_values('height', value)
        self.__height = value

    @property
    def x(self):
        """getter x."""
        return self.__x


    @x.setter
    def x(self, value):
        """settter x."""
        check_values('x', value)
        self.__x = value


    @property
    def y(self):
        """getter y."""
        return self.__y


    @y.setter
    def y(self, value):
        """setter y."""
        check_values('y', value)
        self.__y = value