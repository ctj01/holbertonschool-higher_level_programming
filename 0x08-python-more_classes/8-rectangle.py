#!/usr/bin/python3
"""
Rectangle class definition
"""


class Rectangle:
    """
    class implementation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        property width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        property height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculates area of rectangule
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Perimenter of rectangule
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        str method
        """
        string = ""
        if self.__width is 0 or self.__height is 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            if i is not self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """__repr__

        Returns:
            string: Print rectangule
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """
        compare rectangule
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
