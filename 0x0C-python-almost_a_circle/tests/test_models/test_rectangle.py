#!/usr/bin/python3
from contextlib import redirect_stdout
import inspect
import io
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
import json
from io import StringIO
import sys


class Test_Rectangle(unittest.TestCase):
    """unittest for Rectangle class"""
    @classmethod
    def setUpClass(cls):
        """set up for the rectangle class"""
        Base._Base__nb_objects = 0
        cls.r1 = Rectangle(8, 8)
        cls.r2 = Rectangle(2, 3, 4)
        cls.r3 = Rectangle(3, 5, 7, 8)
        cls.r4 = Rectangle(3, 4, 10, 6)


    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 3)
        self.assertEqual(self.r4.id, 4)

    def test_height(self):
        """Test for functioning height"""
        self.assertEqual(self.r1.height, 8)
        self.assertEqual(self.r2.height, 3)
        self.assertEqual(self.r3.height, 5)
        self.assertEqual(self.r4.height, 4)

    def test_width(self):
        """Test for functioning width"""
        self.assertEqual(self.r1.width, 8)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 3)
        self.assertEqual(self.r4.width, 3)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 4)
        self.assertEqual(self.r3.x, 7)
        self.assertEqual(self.r4.x, 10)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 8)
        self.assertEqual(self.r4.y, 6)

    def test_area(self):
        """test area"""
        self.assertEqual(self.r1.area(), 64)
        self.assertEqual(self.r2.area(), 6)
        self.assertEqual(self.r3.area(), 15)
        self.assertEqual(self.r4.area(), 12)

    def test_save_to_file(self):
        """test regular use of save_to_file"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l = [r1, r2]
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            ls = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_stf_empty(self):
        """test save_to_file with empty list"""
        l = []
        Rectangle.save_to_file(l)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_stf_None(self):
        """test save_to_file with None"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_create(self):
        """test normal use of create"""
        r1 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        r2 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        r1c = Rectangle.create(**r1)
        r2c = Rectangle.create(**r2)
        self.assertEqual("[Rectangle] (2) 4/0 - 2/3", str(r1c))
        self.assertEqual("[Rectangle] (9) 7/8 - 5/6", str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)

    def test_load_from_file_no_file(self):
        """Checks use of load_from_file with no file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_empty_file(self):
        """Checks use of load_from_file with empty file"""
        try:
            os.remove("Rectangle.json")
        except:
            pass
        open("Rectangle.json", 'a').close()
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """test normal use of load_from_file"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        li = [r1, r2]
        Rectangle.save_to_file(li)
        lo = Rectangle.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        r1c = lo[0]
        r2c = lo[1]
        self.assertTrue(type(r1c) is Rectangle)
        self.assertTrue(type(r2c) is Rectangle)
        self.assertEqual(str(r1), str(r1c))
        self.assertEqual(str(r2), str(r2c))
        self.assertIsNot(r1, r1c)
        self.assertIsNot(r2, r2c)
        self.assertNotEqual(r1, r1c)
        self.assertNotEqual(r2, r2c)

    def test_area_args(self):
        """Test too many args are passed for area()"""
        with self.assertRaises(TypeError):
            rec = self.r1.area(1)

    def test_basic_display(self):
        """Test display without x and y"""
        r = Rectangle(2, 3, 0, 0, 1)
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r1.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 8 + "\n") * 8)
        with io.StringIO() as buf, redirect_stdout(buf):
            r.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 2 + "\n") * 3)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.r1.display(1)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 8/8")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/0 - 2/3")
        self.assertEqual(str(self.r3), "[Rectangle] (3) 7/8 - 3/5")
        self.assertEqual(str(self.r4), "[Rectangle] (4) 10/6 - 3/4")

    def test_display_xy(self):
        """Testing the display method with x and y"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r2.display()
            output = buf.getvalue()
            self.assertEqual(output, (" " * 4 + "#" * 2 + "\n") * 3)

    def test_update_args(self):
        """Testing the udpate method with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_args_setter(self):
        """tests that the update method uses setter with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_update_too_many_args(self):
        """test too many args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(1, 1, 1, 1, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_no_args(self):
        """test no args for update"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_update_kwargs(self):
        """Testing the update method with **kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(height=10)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/10")
        r.update(width=11, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 11/10")
        r.update(y=3, width=4, x=5, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 5/3 - 4/10")
        r.update(x=6, height=7, y=8, width=9)
        self.assertEqual(str(r), "[Rectangle] (89) 6/8 - 9/7")

    def test_update_kwargs_setter(self):
        """tests that the update method uses setter with **kwargs"""
        r = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.update(width="hello")
        with self.assertRaises(TypeError):
            r.update(height="hello")
        with self.assertRaises(TypeError):
            r.update(x="hello")
        with self.assertRaises(TypeError):
            r.update(y="hello")
        with self.assertRaises(ValueError):
            r.update(width=-1)
        with self.assertRaises(ValueError):
            r.update(width=0)
        with self.assertRaises(ValueError):
            r.update(height=-1)
        with self.assertRaises(ValueError):
            r.update(height=0)
        with self.assertRaises(ValueError):
            r.update(x=-1)
        with self.assertRaises(ValueError):
            r.update(y=-1)

    def test_mix_args_kwargs(self):
        """tests output for mixed args and kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, 2, 2, 2, 2, width=3, height=3, x=3, y=3, id=3)
        self.assertEqual(str(r), "[Rectangle] (2) 2/2 - 2/2")

    def test_extra_kwargs(self):
        """tests for random kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(hello=2)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")

    def test_to_dict(self):
        """test regular to_dictionary"""
        d1 = self.r1.to_dictionary()
        self.assertEqual({"id": 1, "width": 8, "height": 8, "x": 0, "y": 0},
                         d1)
        d2 = self.r2.to_dictionary()
        self.assertEqual({"id": 2, "width": 2, "height": 3, "x": 4, "y": 0},
                         d2)
        d3 = self.r3.to_dictionary()
        self.assertEqual({"id": 3, "width": 3, "height": 5, "x": 7, "y": 8},
                         d3)
        d4 = self.r4.to_dictionary()
        self.assertEqual({"id": 4, "width": 3, "height": 4, "x": 10,
                          "y": 6}, d4)
        self.assertTrue(type(d1) is dict)
        self.assertTrue(type(d2) is dict)
        self.assertTrue(type(d3) is dict)
        self.assertTrue(type(d4) is dict)
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(**d4)
        self.assertEqual(str(r), str(self.r4))
        self.assertNotEqual(r, self.r4)

    def test_width_typeerror(self):
        """Test non-ints for width raise TypeError"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec = Rectangle("kulundeng", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec = Rectangle(True, 1)

    def test_height_typeerror(self):
        """Test non-ints for height raise TypeError"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec = Rectangle(1, "icampus")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec = Rectangle(1, True)

    def test_x_typeerror(self):
        """Test non-ints for x raise TypeError"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec = Rectangle(1, 1, True)

    def test_y_typeerror(self):
        """Test non-ints for y raise TypeError"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec = Rectangle(1, 1, 1, "kulundeng")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec = Rectangle(1, 1, 1, True)

    def test_width_valueerror(self):
        """Test ints <= 0(negative values) for width raise ValueError"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test ints <= 0 - negative values - for height raise ValueError"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test ints < 0 (negative values) for x raise ValueError"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test ints <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec = Rectangle(1, 1, 1, -1)

    def test_mandatory_width(self):
        """Test that width is a mandatory arg"""
        with self.assertRaises(TypeError):
            rec = Rectangle()

    def test_mandatory_height(self):
        """Test that height is a mandatory arg"""
        with self.assertRaises(TypeError):
            rec = Rectangle(1)

class TestDocstrings(unittest.TestCase):
    """Unittests the Rectangle class documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rec_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_module_docstring(self):
        """unittests for the presence of a module docstring"""
        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_class_docstring(self):
        """unittest for the presence of a class docstring"""
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_func_docstrings(self):
        """unittest for the presence of docstrings in all functions"""
        for func in self.rec_funcs:
            self.assertTrue(len(func[1].__doc__) > 0)

if __name__ == '__main__':
    unittest.main()
