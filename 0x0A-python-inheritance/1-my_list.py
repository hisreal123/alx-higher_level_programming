#!/usr/bin/python3
""" MyList class inheriting from list class"""


class MyList(list):
    """" public instance """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
