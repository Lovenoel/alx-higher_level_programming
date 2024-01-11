#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (None, )  # Return a tuple with None if the sentence is empty
    else:
        return (len(sentence), sentence[0])
