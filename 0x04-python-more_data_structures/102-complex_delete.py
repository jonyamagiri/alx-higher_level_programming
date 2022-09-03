#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    target_keys = []
    for key in a_dictionary.keys():
        target_keys.append(key)
    for idx in target_keys:
        if a_dictionary[idx] == value:
            del a_dictionary[idx]
    return a_dictionary
