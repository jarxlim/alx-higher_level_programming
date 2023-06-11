#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) > 0:
        firstchar = sentence[0]
    else:
        firstchar = None
    return (len(sentence), firstchar)
