#!/usr/bin/python3
""" An empty class called  BaseGeometry"""


class BaseGeometry:
    """" Empty class"""

    def __int__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(self.height) != int:
            raise TypeError("height must be an integer")
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
