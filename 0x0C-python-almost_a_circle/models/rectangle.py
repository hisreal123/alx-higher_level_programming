#!/usr/bin/python3

from base import Base

"""class called Rectangle"""


class Rectangle(Base):
    """ class body
    __width, __height, __x, __y are all private class attribute
     """

    """Private class attribute"""

    # __width = 0
    # __height =

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        def ___init__ is a class constructor
        :params: width, height, x=0, y=0, id=None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        if value <= 0:
            raise ValueError("Width must be > 0.")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        if value <= 0:
            raise ValueError("Height must be > 0.")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("X must be an integer.")
        if value < 0:
            raise ValueError("X must be >= 0.")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("Y must be an integer.")
        if value < 0:
            raise ValueError("Y must be >= 0.")
        self.__y = value

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.height * self.width

    def display(self):
        """Print the Rectangle instance using '#3 characters"""
        for _ in range(self.height):
            print('#' * self.width)
