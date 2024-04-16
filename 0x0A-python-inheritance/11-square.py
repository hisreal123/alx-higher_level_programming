#!/usr/bin/python3

""" class square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """returns the string description of the class"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """" Returning the area of a square"""
        return self.__size * self.__size
