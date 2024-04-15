#!/usr/bin/python3
"""  function that returns True if the object is an instance of a
class that inherited (directly or indirectly)  """


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.
      Args:
          obj (any): The object to check.
          a_class (type): The class to compare the type of obj to.
      Returns:
          Boolean of an instance of a_class.
      """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
