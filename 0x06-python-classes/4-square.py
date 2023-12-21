#!/usr/bin/python3
"""A class Square that defines a square by size"""


class Square:
    """Represent a square"""


    def __init__(self, size=0):
        """initialize  a new Square.
             Args:
               size (int): The size of the new square."""
        self.__size = size


     """gets the size """
    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Get the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Calculates the area of the square"""

    def area(self):  # public instance method
        """Get the area of the square."""
        return self.__size ** 2
