#!/usr/bin/python3
"""
Module test_rectangle.py that contains unittests for class Rectangle
# Executed using command:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_rectangle.py
"""

import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Tests for the class Rectangle
    Methods:
        def test_instance(self)
        def test_area(self)
        def test_display(self)
        def test_str(self)
        def test_update(self)
        def test_to_dictionary(self)
    """

    def setUp(self):
        pass

    def tearDown(self):
        """Tears down object count"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instance(self):
        """Tests instantiation of the class"""
        rec_1 = Rectangle(3, 2)
        rec_2 = Rectangle(8, 7, 0, 0, 12)
        with self.assertRaises(TypeError):
            rec_3 = Rectangle("seven")
            rec_4 = Rectangle(None)
            rec_5 = Rectangle(float('inf'))
            rec_6 = Rectangle(9.5, 9.3)
            rec_7 = Rectangle(-8, 9)
            rec_8 = Rectangle()

        self.assertEqual(rec_1.id, 1)
        self.assertEqual(rec_1._Base__nb_objects, 1)
        self.assertEqual(rec_2.id, 12)
        self.assertEqual(rec_2._Base__nb_objects, 1)

    def test_area(self):
        """Tests area()"""
        rec_1 = Rectangle(3, 2)
        rec_2 = Rectangle(8, 7, 0, 0, 12)
        rec_3 = Rectangle(126, 126)

        self.assertEqual(rec_1.area(), 6)
        self.assertEqual(rec_2.area(), 56)
        self.assertEqual(rec_3.area(), 15876)

    def test_display(self):
        """Tests display()"""
        rec_1 = Rectangle(3, 2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            rec_1.display()
            self.assertEqual(fakeOutput.getvalue(), '###\n###\n')

        rec_2 = Rectangle(5, 3, 1, 2)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            rec_2.display()
            self.assertEqual(
                fakeOutput.getvalue(), '\n\n #####\n #####\n #####\n')

    def test_str(self):
        """Tests __str__()"""
        rec_1 = Rectangle(3, 2)
        rec_2 = Rectangle(8, 7, 0, 0, 12)
        rec_3 = Rectangle(6, 2, 1)
        rec_4 = Rectangle(3, 2, id="engineer")

        self.assertEqual(rec_1.__str__(), '[Rectangle] (1) 0/0 - 3/2')
        self.assertEqual(rec_2.__str__(), '[Rectangle] (12) 0/0 - 8/7')
        self.assertEqual(rec_3.__str__(), '[Rectangle] (2) 1/0 - 6/2')
        self.assertEqual(rec_4.__str__(), '[Rectangle] (engineer) 0/0 - 3/2')

    def test_update(self):
        """Tests update()"""
        rec_1 = Rectangle(3, 2)
        rec_2 = Rectangle(8, 7, 0, 0, 12)
        rec_3 = Rectangle(6, 2, 1)
        rec_4 = Rectangle(3, 2, id="engineer")
        rec_5 = Rectangle(3, 2, id="engineer")

        rec_1.update(5, 7)
        self.assertEqual(rec_1.__str__(), '[Rectangle] (5) 0/0 - 7/2')
        with self.assertRaises(ValueError):
            rec_2.update({'id': 1575, 'x': -5})
            rec_3.update("a string", None, None)
        rec_4.update(None)
        self.assertEqual(rec_4.__str__(), '[Rectangle] (None) 0/0 - 3/2')
        rec_5.update(-9)
        self.assertEqual(rec_5.__str__(), '[Rectangle] (-9) 0/0 - 3/2')

    def test_to_dictionary(self):
        """Tests to_dictionary()"""

        rec_1 = Rectangle(3, 2)
        rec_2 = Rectangle(8, 7, 0, 0, 12)
        rec_3 = Rectangle(6, 2, 1)
        rec_4 = Rectangle(3, 2, id="engineer")

        dict_1 = {'id': 1, 'width': 3, 'height': 2, 'x': 0, 'y': 0}
        dict_2 = {'id': 12, 'width': 8, 'height': 7, 'x': 0, 'y': 0}
        dict_3 = {'id': 2, 'width': 6, 'height': 2, 'x': 1, 'y': 0}
        dict_4 = {'id': 'engineer', 'width': 3, 'height': 2, 'x': 0, 'y': 0}

        self.assertDictEqual(rec_1.to_dictionary(), dict_1)
        self.assertDictEqual(rec_2.to_dictionary(), dict_2)
        self.assertDictEqual(rec_3.to_dictionary(), dict_3)
        self.assertDictEqual(rec_4.to_dictionary(), dict_4)


if __name__ == '__main__':
    unittest.main()
