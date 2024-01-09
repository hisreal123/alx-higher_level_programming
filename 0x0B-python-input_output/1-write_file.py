#!/usr/bin/python3
"""Defines write file module """


def read_file(filename="", test=""):
    """
    write_file function
    write a text file from an (UTF8)
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(test)
