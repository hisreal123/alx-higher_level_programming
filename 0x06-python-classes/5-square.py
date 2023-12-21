#!/usr/bin/python3
"""A class Square that defines a square by size"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialize a new Square.
        Args:
            size (int): The size of the new square."""
        self.__size = size  # Calls the size setter method

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

    """Print to stdout"""

    def my_print(self):
        """Prints a square of a given size."""
        if self.__size == 0:
            print("")

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
