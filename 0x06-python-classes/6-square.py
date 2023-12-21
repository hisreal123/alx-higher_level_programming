#!/usr/bin/python3
"""A class Square that defines a square by size"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initialize a new Square.
        Args:
            size (int): The size of the new square."""
        self.__size = size  # Calls the size setter method
        self.__position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):  # public instance method
        """Calculate and return the area of the square."""
        return self.__size ** 2

    """Getter to get position which is a private instance attribute"""
    @property
    def position(self):
        """return position"""
        return self.__position

    """setter to get position which is a private instance attribute"""
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """Print to stdout"""
    def my_print(self):
        """Print stdout the square with the character"""
        if self.__size == 0:
            print("")

        for i in range(0, self.__size):
            if self.__position[1] > 0:
                print(" " * self.__position[1], end="")
            print("#" * self.__size)
