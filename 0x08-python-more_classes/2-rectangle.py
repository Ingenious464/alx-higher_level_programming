#!/usr/bin/python3
"""Defines a Rectangle Class"""


class Rectangle:
    """Defines a rectangle."""

    def _init_(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._width = value
             else:
                 raise ValueError('width must be >= 0')
        else:
             raise TypeError('width must be an integer')

    @property
    def width(self):
        """Gets the height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self._height = value
             else:
                 raise ValueError('height must be >= 0')
        else:
             raise TypeError('height must be an integer')

    def area(self):
        """Returns the area of the rectangle"""
        return int(self._width) * int(self._height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * int(self._width)) + (2 * int(self._height))
