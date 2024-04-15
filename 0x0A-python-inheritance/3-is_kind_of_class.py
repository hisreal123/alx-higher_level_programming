#!/usr/bin/python3
""" returns True if the object is an instance of, or if the
object is an instance of a class that inherited from  the specified class ;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of a given class.
      Args:
          obj (any): The object to check.
          a_class (type): The class to compare the type of obj to.
      Returns:
          Boolean of an instance of a_class.
      """

    if isinstance(obj, a_class):
        return True
    else:
        return False
