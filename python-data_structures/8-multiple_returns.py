#!/usr/bin/python3
def multiple_returns(sentence):
    first_char = ""
    lenght = len(sentence)
    if lenght == 0:
        first_char = None
    else:
        first_char = sentence[0]

    return lenght, first_char
