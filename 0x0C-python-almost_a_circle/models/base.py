#!/usr/bin/python3

"""class called Base"""


class Base:
    """ class body
    __nb_object is a private class attribute
     """

    """Private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        def ___init__ is a class constructor
        :param id:
        """

        if id is not None:
            """public class attribute."""
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
