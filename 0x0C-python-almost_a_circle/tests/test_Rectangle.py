#!/usr/bin/python3

"""
This test is for the Rectangle class
Type: Unittest
"""
from unittest import  TestCase, main
from models.base import Base as B
from models.rectangle import Rectangle
from io import StringIO
import sys


class Test_ClassRectangle(TestCase):

    def test_id(self):
        """
        testing  id
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

    def test_area(self):
        """
        test area method
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """
        testing display method
        """
        out = StringIO()
        sys.stdout = out
        r1 = Rectangle(4, 6)
        r1.display()
        sys.stdout = sys.__stdout__
        assert  out.getvalue() == '####\n' * 6

    def test_str(self):
        """
        test str method
        """
        out = StringIO()
        sys.stdout = out
        r = Rectangle(2, 8, 2, 7, 5)
        print(r)
        sys.stdout = sys.__stdout__
        assert out.getvalue() == "[Rectangle] (5) 2/7 - 2/8\n"

    def test_update(self):
        """
        test update method
        """
        out = StringIO()
        sys.stdout = out
        r = Rectangle(8, 6, 9, 12)
        r.update(8)
        r.update(8, 2)
        r.update(8, 2, 3)
        r.update(8, 2, 3, 4)
        r.update(8, 2, 3, 4, 5)
        print(r)
        sys.stdout = sys.__stdout__
        assert out.getvalue() == "[Rectangle] (8) 4/5 - 2/3\n"
