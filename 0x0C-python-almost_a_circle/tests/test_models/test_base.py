#!/usr/bin/python3
"""
Module test_base.py that contains unittests for class Base
# Executed using command:
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base.py
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the class Base
    Methods:
        def test_instance(self)
        def test_to_json_string(self)
        def test_from_json_string(self)
        def test_create(self)
        def test_save_to_file(self)
        def test_load_from_file(self)
    """

    def setUp(self):
        pass

    def tearDown(self):
        """Tears down object count"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_instance(self):
        """Tests instantiation of the class"""
        base_1 = Base()
        base_2 = Base(7)
        base_3 = Base(2.5)
        base_4 = Base(float('inf'))
        base_5 = Base("engineer")
        base_6 = Base(["list", 5, 8.9])
        base_7 = Base(None)

        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 7)
        self.assertEqual(base_3.id, 2.5)
        self.assertEqual(base_4.id, float('inf'))
        self.assertEqual(base_5.id, "engineer")
        self.assertEqual(base_6.id, ["list", 5, 8.9])
        self.assertEqual(base_7.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_to_json_string(self):
        """Tests to_json_string()"""
        b1 = [{"hi": 1, "aye": "hola"}]
        b2 = [{"hey": 3}]
        b3 = None
        b4 = "an object"
        b5 = 791
        b6 = [[7, 9, 1]]
        b7 = []

        self.assertCountEqual(
            Base.to_json_string(b1),
            '[{"hi":1, "aye": "hola"}]')
        self.assertCountEqual(Base.to_json_string(b2), '[{"hey": 3}]')
        self.assertCountEqual(Base.to_json_string(b3), '[]')
        self.assertCountEqual(Base.to_json_string(b4), '"an object"')
        with self.assertRaises(TypeError):
            Base.to_json_string(b5)
        self.assertCountEqual(Base.to_json_string(b6), '[[7, 9. 1]]')
        self.assertCountEqual(Base.to_json_string(b7), '[]')

    def test_from_json_string(self):
        """Testing from_json_string(), uses to_json_string to format,
        anything not in format should return []
        """
        b1 = [{"hi": 1, "aye": "hola"}]
        res_1 = Base.to_json_string(b1)
        b2 = [{"hey": 3}]
        res_2 = Base.to_json_string(b2)
        b3 = None
        res_3 = Base.to_json_string(b3)
        b4 = "an object"
        res_4 = Base.to_json_string(b4)
        b5 = 791
        b6 = [[7, 9, 1]]
        res_6 = Base.to_json_string(b6)
        b7 = []
        res_7 = Base.to_json_string(b7)

        self.assertEqual(Base.from_json_string(res_1), b1)
        self.assertEqual(Base.from_json_string(res_2), b2)
        self.assertEqual(Base.from_json_string(res_3), [])
        self.assertEqual(Base.from_json_string(res_4), b4)
        self.assertEqual(Base.from_json_string(res_5), [])
        self.assertEqual(Base.from_json_string(res_6), b6)
        self.assertEqual(Base.from_json_string(res_7), b7)
        self.assertEqual(Base.from_json_string(b1), [])
        self.assertEqual(Base.from_json_string(b3), [])
        self.assertEqual(Base.from_json_string(b7), [])

    def test_create(self):
        """Tests create()"""
        bs1 = {'id': 1, 'width': 1, 'height': 2, 'x': 2, 'y': 2}
        rec1 = Rectangle.create(**bs1)
        self.assertEqual(rec1.__str__(), '[Rectabgle] (1) 2/2 - 1/2')

        bs2 = {'id': 2, 'size': 3, 'x': 4, 'y': 5}
        sqr1 = Square.create(**bs2)
        self.assertEqual(sqr1.__str__(), '[Square] (2) 4/5 - 3')

        bs3 = {'id': 1, 'width': "one", 'height': 2, 'x': 2, 'y': 2}
        bs4 = {'id': 2, 'size': "three", 'x': 4, 'y': 5}
        with self.assertRaises(TypeError):
            rec2 = Rectangle.create(**bs3)
            sqr2 = Square.create(**bs4)

    def test_save_to_file(self):
        """Tests save_to_file()"""
        rec_1 = Rectangle(10, 7, 2, 8)
        rec_2 = Rectangle(2, 4)
        sqr_1 = Square(10, 7, 2)
        sqr_2 = Square(8)

        rec_save = Rectangle.save_to_file([rec_1, rec_2])
        sqr_save = Square.save_to_file([sqr_1, sqr_2])

        self.assertTrue(os.path.isfile('Rectangle.json'))
        self.assertTrue(os.path.isfile('Square.json'))

    def test_load_from_file(self):
        """Tests load_from_file()"""

        rect_1 = Rectangle(10, 7, 2, 8)
        rect_2 = Rectangle(2, 4)
        sq_1 = Square(10, 7, 2)
        sq_2 = Square(8)

        rect_save = Rectangle.save_to_file([rect_1, rect_2])
        sq_save = Square.save_to_file([sq_1, sq_2])

        rect_list = Rectangle.load_from_file()
        sq_list = Square.load_from_file()

        self.assertIsInstance(rect_list[0], Rectangle)
        self.assertIsInstance(rect_list[1], Rectangle)
        self.assertIsInstance(sq_list[0], Square)
        self.assertIsInstance(sq_list[1], Square)

        self.assertEqual(rect_list[0].__str__(), '[Rectangle] (1) 2/8 - 10/7')
        self.assertEqual(rect_list[1].__str__(), '[Rectangle] (2) 0/0 - 2/4')
        self.assertEqual(sq_list[0].__str__(), '[Square] (3) 7/2 - 10')
        self.assertEqual(sq_list[1].__str__(), '[Square] (4) 0/0 - 8')


if __name__ == '__main__':
    unittest.main()
