#!/usr/bin/python3


"""
Defines an Empty Rectangle Class
"""


class Rectangle:
    """ class body"""

    def __init__(self, width=0, height=0):
        self.__height = None
        self.__width = None
        self.width = width
        self.height = height

    @property
    def width(self):
        """width setter"""
        return self.__width

    @width.setter
    def width(self, new_width):
        """width getter """
        if not isinstance(new_width, int):
            raise TypeError("width must be an integer")

        if new_width < 0:
            raise ValueError("width must be >= 0")

        self.__width = new_width

    @property
    def height(self):
        """height getter """
        return self.__height

    @height.setter
    def height(self, new_height):
        """height setter """
        if not isinstance(new_height, int):
            raise TypeError("height must be an integer")

        if new_height < 0:
            raise ValueError("height must be >= 0")

        self.__height = new_height

    def area(self):
        """
        Calculates the area of a Rectangle instance
        Returns:
        Area of the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of a Rectangle instance
        Returns:
        Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
