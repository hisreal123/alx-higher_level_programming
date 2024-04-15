#!/usr/bin/python3
""" checks if the obj is an instance of a class"""


def is_same_class(obj, a_class):

    if isinstance(obj, a_class):
        return True
    else:
        return False

    