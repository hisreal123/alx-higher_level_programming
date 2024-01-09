#!/usr/bin/python3
"""Defines write file module """


def read_file(filename="", test=""):
    """
    Write a string to a UTF8 text file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(test)
