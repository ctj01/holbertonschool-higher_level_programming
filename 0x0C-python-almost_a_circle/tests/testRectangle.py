#!/usr/bin/python3
"""
This test is for the Rectangle class
Type: Unittest
"""
from unittest import  TestCase
from models.base import Base
from models.rectangle import Rectangle


class Test_ClassRectangle(TestCase):

    def Testid(self):
        """
        checking id
        """
        R = Rectangle(4, 6)
        self.assertEqual(R.id, 1)