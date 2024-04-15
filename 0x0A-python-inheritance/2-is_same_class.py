#!/usr/bin/python3
""" checks if the obj is an instance of a class"""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.
      Args:
          obj (any): The object to check.
          a_class (type): The class to compare the type of obj to.
      Returns:
          Boolean of an instance of a_class.
      """

    if type(obj) == a_class:
        return True
    else:
        return False
