#!/usr/bin/python3
"""
This test is for the base class
Type: Unittest
Functions:
"""
import unittest
from models.base import Base as B
from models.rectangle import Rectangle
from models.square import Square


class t_Base_class(unittest.TestCase):
    """Base class unit test"""

    def test_id_input(self):
        """checking the entry of the id argument"""
        B._Base__nb_objects = 0

        b1 = B()
        self.assertEqual(b1.id, 1)

        b2 = B(17)
        self.assertEqual(b2.id, 17)

        b3 = B(-17)
        self.assertEqual(b3.id, -17)

    def test_id_instaningObjects(self):
        """checking the increase of the id argument"""
        B._Base__nb_objects = 0

        b1 = B()
        self.assertEqual(b1.id, 1)

        b2 = B()
        self.assertEqual(b2.id, 2)

        b3 = B()
        self.assertEqual(b3.id, 3)

        b4 = B()

        self.assertEqual(b4.id, 4)

        b5 = B()
        self.assertEqual(b5.id, 5)

    def test_to_json_string(self):
        """
        check JSON string representation of dictionary list.
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = B.to_json_string([dictionary])
        self.assertCountEqual(
            dictionary, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_save_to_file(self):
        """
        check if save a obj as JSON string in json file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            txt = file.read()

    def test_create(self):
        """
        check if return a instance with all attributes already set.
        """
        B._Base__nb_objects = 0

        d = {'id': 5, 'width': 3, 'height': 7, 'x': 2, 'y': 1}
        r1 = Rectangle.create(**d)
        self.assertEqual(r1.to_dictionary(), d)
        self.assertEqual(B._Base__nb_objects, 1)

        s2 = Square(5)
        d4 = s2.to_dictionary()
        s5 = Square.create(**d4)
        self.assertEqual(s5.to_dictionary(), d4)
        self.assertEqual(B._Base__nb_objects, 3)

    def test_load_from_file(self):

        r = Rectangle(2, 4)
        d = r.to_dictionary()
        Rectangle.save_to_file([r])
        s = Rectangle.load_from_file()
        self.assertIsInstance(s[0], Rectangle)
        self.assertDictEqual(s[0].to_dictionary(), d)
