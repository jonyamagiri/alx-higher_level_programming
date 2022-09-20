#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer"""
    
    def test_max_int(self):
        """Test for when all values of list are ints"""
        self.assertEqual(max_integer([1, 5, 3, 4]), 5)
        self.assertEqual(max_integer([1, 2, 3.7, 11]), 11)

    def test_max_empty(self):
        """Test for when list is empty; None is returned"""
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer(), None)

    def test_max_one(self):
        """Test for when list has one element"""
        self.assertEqual(max_integer([8]), 8)

    def test_max_negative(self):
        """Test for when list element is negative"""
        self.assertEqual(max_integer([1, 2, 3.7, -11]), 3.7)
        self.assertEqual(max_integer([-1, -2, -3.7, -11]), -1)

    def test_max_datatype(self):
        """Test for type of data entered. If not integer, raise errors."""
        self.assertRaises(TypeError, max_integer, [5, "9", 16])
        self.assertRaises(TypeError, max_integer, ["twenty", "9", 16, 3])

    def test_max_strings(self):
        """Test for when list has string elements"""
        self.assertEqual(max_integer("27451"), '7')
        self.assertEqual(max_integer("lazyfox"), 'z')
        self.assertEqual(max_integer(["l", "a", "z", "y", "f", "x"]), 'z')


if __name__ == "__main__":
    unittest.main()
