#!/usr/bin/python3
"""Defines read file module """


def append_write(filename="", test=""):

    """read_file function reads a text file(UTF8) and prints it result to stdout """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(test)
