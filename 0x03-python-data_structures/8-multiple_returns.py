#!/usr/bin/python3
def multiple_returns(sentence):
    i = len(sentence)
    c = ""
    if i == 0:
        c = None
    else:
        c = sentence[0]
    return (i, c)
