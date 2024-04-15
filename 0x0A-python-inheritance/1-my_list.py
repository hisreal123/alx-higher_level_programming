#!/usr/bin/python3
""" Defines available attributes/methods of an object"""

""" MyList class inheriting from list class"""


class MyList(list):
    """" public instance """

    def print_sorted(self):
        if isinstance(list, int):
            sorted_list = sorted(self)
            print(sorted_list)
