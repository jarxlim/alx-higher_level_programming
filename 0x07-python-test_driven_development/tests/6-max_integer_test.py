#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """a unittes class for max_integer"""
    def test_ints_unordered(self):
        """tstst a list unordered integers"""
        u_int = [45, 6, 80, 23, 9]
        self.assertEqual(max_integer(u_int), 80)

    def test_ints_ordered(self):
        '''tests a list of ordered integers'''
        o_int = [6, 9, 23, 45, 80]
        self.assertEqual(max_integer(o_int), 80)
        
    def test_one_element(self):
        """tests just one element"""
        int_one = [4]
        self.assertEqual(max_integer(int_one), 4)

    def floats_tst(self):
        '''tests a list of floats'''
        floats = [5.3, 4.3, -9.6, 6.2, 2.1]
        self.assertEqual(max_integer(floats), 6.2)
    
    def floats_and_ints(self):
        """tests a lists of floats and ints"""
        f_and_i = [3, 2.3, 3.3, 4, 1.2, 2]
        self.assertEqual(max_integer(f_and_i), 4)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        ne_l = [-46, -5, -75, -1, -10]
        self.assertEqual(max_integer(ne_l), -1)

    def test_non_int(self):
        """Tests for a non-int in list"""
        mixed = [5, 7, "Chike", 4, 5, "Hello"]
        with self.assertRaises(TypeError):
            max_integer(mixed)

    def test_none(self):
        """Tests for passing non"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_args(self):
        """Tests for no arguments"""
        self.assertIsNone(max_integer())

if __name__ == "__main__":
    unittest.main()
