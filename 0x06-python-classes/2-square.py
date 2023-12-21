#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialize  a new Square.
        Args:
            size (int): The size of the new square."""
        self.__size = size

        if int(size):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
