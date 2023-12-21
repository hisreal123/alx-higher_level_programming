#!/usr/bin/python3
"""A class Square that defines a square by size"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialize  a new Square.
             Args:
               size (int): The size of the new square."""
        self.__size = size  # private instance attribute"

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """Calculates the area of the square"""

    def area(self):  # public instance method
        """Get the size of the square."""
        return self.__size ** 2
