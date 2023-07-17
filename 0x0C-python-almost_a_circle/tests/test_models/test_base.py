#!/usr/bin/python3
import unittest
from models.base import Base
"""
    test cases creation for the base module
"""


class TestBase(unittest.TestCase):
    """Testing base"""
    def test_init(self):
        """sending id number"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_nb_objects(self):
        """Sending id for nb object"""
        b1 = Base()
        self.assertEqual(Base._Base__nb_objects, 3)

        b2 = Base()
        self.assertEqual(Base._Base__nb_objects, 4)

        b3 = Base()
        self.assertEqual(Base._Base__nb_objects, 5)

if __name__ == '__main__':
    unittest.main()
