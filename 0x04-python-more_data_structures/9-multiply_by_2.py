#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    doubles_dictionary = a_dictionary.copy()
    for key in doubles_dictionary:
        doubles_dictionary[key] *= 2
    return doubles_dictionary
