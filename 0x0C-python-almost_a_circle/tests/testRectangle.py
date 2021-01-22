#!/usr/bin/python3
"""
This test is for the Rectangle class
Type: Unittest
"""
import sys
import  os
sys.path.insert(1, os.getcwd())

from unittest import  TestCase, main
from models.base import Base
from models.rectangle import Rectangle


class Test_ClassRectangle(TestCase):

    def Testid(self):
        """
        checking id
        """
        R = Rectangle(4, 6)
        self.assertEqual(R.id, 1)

if __name__ == '__main__':
    main()