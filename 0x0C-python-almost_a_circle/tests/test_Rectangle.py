#!/usr/bin/python3

"""
This test is for the Rectangle class
Type: Unittest
"""
from unittest import  TestCase, main
from models.base import Base
from models.rectangle import Rectangle


class Test_ClassRectangle(TestCase):

    def test_id(self):
        """
        checking id
        """

        Rec = Rectangle(5 , 6)
        self.assertEqual(Rec.id, 1)
