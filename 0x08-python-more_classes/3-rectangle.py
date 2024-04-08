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
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

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
        return self.__width * self._height

    def perimeter(self):
        if self.__width == 0 or self._height == 0:
            return ""
        rectantle_str = ""
        for _ in range(self._height):
            rectantle_str += "#" * self.__width + "\n"
        return rectantle_str.rsplit()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self._height)

