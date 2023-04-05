#!/usr/bin/python3
"""Defines a Rectangle Class"""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
             raise TypeError('width must be an integer')

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
             raise TypeError('height must be an integer')

    def area(self):
        """Returns the area of the rectangle"""
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * int(self.__width)) + (2 * int(self.__height))

    def __str__(self):
        """Prints the rectangle with the character #"""
        strn = ""
        if self.__width == 0 or self.__height == 0:
            return strn
        strn += ('#' * self.__width + '\n') * self.__height
        return strn[:-1]
