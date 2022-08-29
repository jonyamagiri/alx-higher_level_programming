#!/usr/bin/python3
def multiple_returns(sentence):
    string_length = len(sentence)
    if string_length != 0:
        first_character = sentence[0]
    else:
        first_character = None
    return (string_length, first_character)
