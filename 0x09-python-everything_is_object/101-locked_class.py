#!/usr/bin/python3
""" A class called LockedClass"""


class LockedClass:
    def __setattr__(self, name, value):
        if not hasattr(self, name) and name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute {}".format(name))
        super().__setattr__(name, value)
