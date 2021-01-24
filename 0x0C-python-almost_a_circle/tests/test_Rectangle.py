#!/usr/bin/python3

"""
This test is for the Rectangle class
Type: Unittest
"""
from unittest import  TestCase, main
from models.base import Base as B
from models.rectangle import Rectangle


class Test_ClassRectangle(TestCase):

    def test_id(self):
        """
        checking id
        """
        B._Base__nb_objects = 0  

        Reca = Rectangle(5 , 6)
        self.assertEqual(Reca.id, 1)

        Recb = Rectangle(4, 6 , 9 , 8 ,8)
        self.assertEqual(Recb.id, 8)

    def  test_exceptions(self):
        """
        testing exceptions
        """
        B._Base__nb_objects = 0
        self.assertRaisesRegex(TypeError, "height must be an integer", Rectangle, 1, "u")
        self.assertRaisesRegex(TypeError, "y must be an integer", Rectangle, 1, 2, 8, "y")
        self.assertRaisesRegex(ValueError, "width must be > 0", Rectangle, 0, 2)
