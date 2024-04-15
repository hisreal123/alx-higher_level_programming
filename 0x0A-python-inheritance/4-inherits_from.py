#!/usr/bin/python3
"""  function that returns True if the object is an instance of a
class that inherited (directly or indirectly)  """


def inherits_from(obj, a_class):

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
