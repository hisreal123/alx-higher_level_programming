#!/usr/bin/python3
"""Defines read file module """


def append_write(filename="", test=""):
    """Appends a string to the end of a UTF8 text file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(test)
