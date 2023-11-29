#!/usr/bin/python3
def to_uper(character):
    if 97 <= ord(character) <= 122:
        return ord(character) - 32
    else:
        return ord(character)


def uppercase(strr):
    new = ""
    for character in strr:
        new += "%c" % to_uper(character)
    print("{:s}".format(new))
