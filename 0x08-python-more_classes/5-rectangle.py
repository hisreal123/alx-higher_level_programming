#!/usr/bin/python3


"""
Defines an Empty Rectangle Class
"""


class Rectangle:
    """ class body"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property to retrieve the width """
        return self._width

    @width.setter
    def width(self, value):
        """ property setter for width that has been retrieve above"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        pass
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self._height):
            rectangle_str += "#" * self._width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        print("Bye rectangle...")
