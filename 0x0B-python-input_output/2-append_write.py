#!/usr/bin/python3
"""Defines read file module """


def append_write(filename="", test=""):
    """
    read_file function
    reads a text file (UTF8) and prints it result to stdout
    """
    with open(filename, 'r', encoding='utf-8') as f:
        number_of_line = f.read()

    number_of_line += test

    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(number_of_line)
