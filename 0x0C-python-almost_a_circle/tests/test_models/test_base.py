#!/usr/bin/python3
"""
Module test_base.py that contains unittests for class Base
# Executed using command: 
    python3 -m unittest discover tests
    python3 -m unittest tests/test_models/test_base.py
    python3 -m unittest -v tests/test_models/test_base.py  # verbose
"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the class Base
    Methods:
        
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







if __name__ == '__main__':
    unittest.main()
