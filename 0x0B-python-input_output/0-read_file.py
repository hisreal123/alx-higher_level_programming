#!/usr/bin/python

"""  function read_file reads a file and return's the value """


def read_file(filename=""):
    """ within the function body"""
    with open(filename, encoding="utf-8") as f:
        """ this opens the file, in encoding utf-8 which means it should be readable"""
        return f.read()
