#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        fIndex = None
        snLen = len(sentence)
        return snLen, fIndex

    else:
        fIndex = sentence[0]
        snLen = len(sentence)

        return snLen, fIndex

