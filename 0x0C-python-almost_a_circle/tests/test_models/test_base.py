#!/usr/bin/python3
"""Defines unittests for base.py"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import models.rectangle
import models.square
import models.base


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class"""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

if __name__ == "__main__":
    unittest.main()
