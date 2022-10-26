#!/usr/bin/python3
"""
Module test_square.py that contains unittests for class Square
# Executed using command:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_square.py
"""


import unittest
import os
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests for the class Square
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
        sqr_1 = Square(5)
        sqr_2 = Square(id="hey", size=3)
        with self.assertRaises(ValueError):
            sqr_3 = Square(-5, 3, 4)
            sqr_4 = Square(9.5, 9.3)
            sqr_5 = Square(float('inf'))
            sqr_6 = Square("an engineer")
            sqr_7 = Square(None)

        with self.assertRaises(TypeError):
            sqr_8 = Square(7, "goodbye")
            sqr_9 = Square(6, None)
            sqr_10 = Square(3, float('inf'))
            sqr_11 = Square(8, 9.3)
            sqr_12 = Square()

        self.assertEqual(sqr_1.id, 1)
        self.assertEqual(sqr_1._Base__nb_objects, 3)
        self.assertEqual(sqr_2.id, 'hey')
        self.assertEqual(sqr_2._Base__nb_objects, 3)

    def test_area(self):
        """Tests area()"""
        sqr_1 = Square(7)
        sqr_2 = Square(127, 0, 0, "goodday")
        sqr_3 = Square(id="whitehat", size=3, x=1, y=0)

        self.assertEqual(sqr_1.area(), 49)
        self.assertEqual(sqr_2.area(), 16129)
        self.assertEqual(sqr_3.area(), 9)

    def test_display(self):
        """Tests display()"""
        sqr_1 = Square(4)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            sqr_1.display()
            self.assertEqual(fakeOutput.getvalue(), '####\n####\n####\n####\n')

        sqr_2 = Square(id="whitehat", size=3, x=1, y=0)
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            sqr_2.display()
            self.assertEqual(fakeOutput.getvalue(), ' ###\n ###\n ###\n')

    def test_str(self):
        """Tests __str__()"""
        sqr_1 = Square(7)
        sqr_2 = Square(5, 3)
        sqr_3 = Square(2, 4, 6, 8)
        sqr_4 = Square(id="whitehat", size=3, x=1, y=0)

        self.assertEqual(sqr_1.__str__(), '[Square] (1) 0/0 - 7')
        self.assertEqual(sqr_2.__str__(), '[Square] (2) 3/0 - 5')
        self.assertEqual(sqr_3.__str__(), '[Square] (8) 4/6 - 2')
        self.assertEqual(sqr_4.__str__(), '[Square] (whitehat) 1/0 - 3')

    def test_update(self):
        """Tests update()"""
        sqr_1 = Square(7)
        sqr_2 = Square(5, 3)
        sqr_3 = Square(2, 4, 6, 8)
        sqr_4 = Square(id="whitehat", size=3, x=1, y=0)

        sqr_1.update(5, 3, 1, 7)
        self.assertEqual(sqr_1.__str__(), '[Square] (5) 1/7 - 3')
        sqr_2.update(2, 4, 6, id="eight")
        self.assertEqual(sqr_2.__str__(), '[Square] (eight) 3/0 - 5')
        with self.assertRaises(ValueError):
            sqr_3.update("blackhat", -8)
            sqr_4.update(x=3.7)

    def test_to_dictionary(self):
        """Tests to_dictionary()"""

        sqr_1 = Square(7)
        sqr_2 = Square(8, 7)
        sqr_3 = Square(6, 4, 2, 8)
        sqr_4 = Square(3, 2, id="engineer")

        dict_1 = {'id': 1, 'size': 7, 'x': 0, 'y': 0}
        dict_2 = {'id': 2, 'size': 8, 'x': 7, 'y': 0}
        dict_3 = {'id': 8, 'size': 6, 'x': 4, 'y': 2}
        dict_4 = {'id': 'engineer', 'size': 3, 'x': 2, 'y': 0}

        self.assertDictEqual(sqr_1.to_dictionary(), dict_1)
        self.assertDictEqual(sqr_2.to_dictionary(), dict_2)
        self.assertDictEqual(sqr_3.to_dictionary(), dict_3)
        self.assertDictEqual(sqr_4.to_dictionary(), dict_4)


if __name__ == '__main__':
    unittest.main()
